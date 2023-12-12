from MyMods.Matrix import Matrix
from day10.pipe import Pipe


class PipeMap(Matrix):
    def __init__(self, dimj, dimi):
        super().__init__(dimj, dimi, base=".")
        self.start = None
        self.distance = 1
        self.position_1 = None
        self.position_2 = None

    def get_start(self):
        for j in range(self.dimj):
            for i in range(self.dimi):
                if self.grid[i][j].get_value() == 'S':
                    self.start = j, i
                    self.position_1 = j, i
                    self.position_1 = j, i

    def add_lines(self, lines):
        for j in range(self.dimj):
            for i in range(self.dimi):
                p = Pipe(lines[j][i], (j, i))
                self.grid[j][i] = p

    def walk(self):
        self.position_1 = self.grid[3][0]
        print(self.position_1, type(self.position_1))
        self.position_1.set_distance_to_start(self.distance)
        self.position_2 = self.grid[2][1]
        print(self.position_2, type(self.position_2))
        self.position_2.set_distance_to_start(self.distance)
        while True:
            self.distance += 1
            # get the two neighbors of S (BIG S: (109,28) -> (100,28) + (100,29)
            # small S : (2, 0) -> (3, 0) + (2, 1)
            # walk one side and add one to distance
            new_coords1 = self.position_1.get_neighbor(self.position_1.coords)
            print(new_coords1)
            self.position_1 = self.grid[new_coords1[0]][new_coords1[1]]
            self.position_1.set_distance_to_start(self.distance)
            print("walk 1 : ", self.position_1)
            # walk other side and add one to distance
            old_position2 = self.position_2
            print(old_position2.coords)
            self.position_2 = None
            new_coords2 = old_position2.get_neighbor(old_position2.coords)
            self.position_2 = self.grid[old_position2[0]][old_position2[1]]
            self.position_2.set_distance_to_start(self.distance)
            print("walk 2 : ", self.position_2)
            # where they meet is furthest
            if self.position_1.coords == self.position_2.coords:
                break
        print("Distance : ", self.distance)

    def __str__(self):
        res = ""
        for j in range(self.dimj):
            for i in range(self.dimi):
                res += str(self.grid[j][i])
            res += "\n"
        return res

