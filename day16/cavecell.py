class CaveCell:
    def __init__(self, value, coords):
        self.DIRECTIONS = {2: "E", 3: "S", 4: "W", 1: "N"}
        self.coords = coords
        self.value = value
        self.from_cell = None
        self.to_cell = []
        self.visited = False
        self.direction = self.DIRECTIONS[2]
        self.calc_next()

    def get_coords(self):
        return self.coords[0], self.coords[1]

    def set_value(self, new_value):
        print("new vlaue : ", new_value, type(new_value))
        self.value = new_value

    def get_value(self):
        return self.value

    def dead_end(self):
        return self.to_cell == 0

    def get_next_cell(self):
        return self.to_cell[0], self.to_cell[1]

    def get_from_cell(self):
        return self.from_cell[0], self.from_cell[1]

    def crossroad(self):
        return len(self.to_cell) > 1

    def calc_from(self):
        j, i = self.from_cell.get_coords()
        if j == self.coords[0] + 1:
            return self.DIRECTIONS[3]
        elif j == self.coords[0] - 1:
            return self.DIRECTIONS[1]
        elif i == self.coords[1] + 1:
            return self.DIRECTIONS[4]
        elif i == self.coords[1] - 1:
            return self.DIRECTIONS[2]

    def go_direction(self, direction):
        new_j, new_i = self.coords
        if direction == "N":
            new_j -= 1
        elif direction == "S":
            new_j += 1
        elif direction == "W":
            new_i -= 1
        elif direction == "E":
            new_i += 1
        self.to_cell = new_j, new_i
        return new_j, new_i


    def calc_next(self):
        from_dir = self.calc_from()
        if self.value == "|":
            if from_dir == "N":
                self.to_cell = self.go_direction(from_dir)
            self.to_cell = self.calc_next_vertical()
        elif self.value == "-":
            self.to_cell = self.calc_next_horizontal()
        elif self.value == "/":
            self.to_cell = self.calc_next_slash()
        elif self.value == "*":
            self.to_cell = self.calc_next_backslash()
        elif self.value == ".":
            self.to_cell = self.calc_next_space()

    def __str__(self):
        return self.value
