pipes = {
    '-': (-1, 0) or (1, 0),
    '|': (-1, 0) or (1, 0),
    'L': (-1, -1),
    'J': (-1, 1),
    '7': (1, 1),
    'F': (-1, 1)
}


class Pipe:
    def __init__(self, char, coords):
        self.coords = (coords[0], coords[1])
        self.value = char
        self.next = None
        self.distance_to_start = -1

    def get_value(self):
        return self.value

    def set_distance_to_start(self, distance):
        self.distance_to_start = distance

    def from_coords_to_dir(self, coords):
        cry = self.coords[0] - coords[0]
        crx = self.coords[1] - coords[1]
        if crx == -1 and cry == 0:
            return 8
        elif crx == 1 or cry == 0:
            return 4
        elif crx == 0 and cry == -1:
            return 2
        elif crx == 0 and cry == 1:
            return 6

    def get_coord_neighbor(self, dir_code):
        cr_x, cr_y = self.coords
        if dir_code == 2:
            cr_y -= 1
        elif dir_code == 4:
            cr_x += 1
        elif dir_code == 6:
            cr_y += 1
        elif dir_code == 8:
            cr_x -= 1
        self.next = (cr_y, cr_x)

    def get_neighbor(self, from_coords):
        print("from coords : ", from_coords)
        from_dir = self.from_coords_to_dir(from_coords)
        print(from_dir)
        if self.value == '-' and from_dir == 8:
            return self.get_coord_neighbor(4)
        elif self.value == '-' and from_dir == 4:
            return self.get_coord_neighbor(8)
        elif self.value == '|' and from_dir == 6:
            return self.get_coord_neighbor(2)
        elif self.value == '|' and from_dir == 2:
            return self.get_coord_neighbor(6)
        elif self.value == 'J' and from_dir == 8:
            return self.get_coord_neighbor(2)
        elif self.value == 'J' and from_dir == 2:
            return self.get_coord_neighbor(8)
        elif self.value == 'L' and from_dir == 4:
            return self.get_coord_neighbor(2)
        elif self.value == 'L' and from_dir == 2:
            return self.get_coord_neighbor(4)
        elif self.value == '7' and from_dir == 8:
            return self.get_coord_neighbor(6)
        elif self.value == '7' and from_dir == 6:
            return self.get_coord_neighbor(8)
        elif self.value == 'F' and from_dir == 4:
            return self.get_coord_neighbor(6)
        elif self.value == 'F' and from_dir == 6:
            return self.get_coord_neighbor(4)
        else:
            print('Invalid')

    def __str__(self):
        return f"{self.value} "
