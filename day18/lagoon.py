import re

from MyMods.Matrix import Matrix
from day18.dig import Dig
from day18.vertices import Vertices


class Lagoon(Matrix):
    def __init__(self):
        super().__init__(1000, 1000)
        self.directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        self.current_position = (500, 200)
        self.vertices = []
        self.add_lines2()
        self.count()

    def add_lines2(self):
        for j in range(self.dimj):
            for i in range(self.dimi):
                self.grid[j][i] = Dig((j, i))

    def add_operator(self, dataline):
        pattern = r"^(?P<direction>[UDLR]) (?P<steps>\d+) \(#(?P<color>[0-9a-f]{6})\)$"
        matches = re.findall(pattern, dataline)[0]
        direction = matches[0][0]
        steps = int(matches[1])
        color = matches[2]
        self.do_operation(direction, steps, color)

    def do_operation(self, direction, steps, color):
        j, i = self.current_position
        end = None
        if direction == 'U':
            for x in range(1, steps + 1):
                self.grid[j - x][i].add_color(color)
            self.current_position = (j - steps, i)
        elif direction == 'D':
            for x in range(1, steps + 1):
                self.grid[j + x][i].add_color(color)
            self.current_position = (j + steps, i)
        elif direction == 'L':
            for x in range(1, steps + 1):
                self.grid[j][i - x].add_color(color)
            self.current_position = (j, i - steps)
        elif direction == 'R':
            for x in range(1, steps + 1):
                self.grid[j][i + x].add_color(color)
            self.current_position = (j, i + steps)
        v = Vertices((j, i), self.current_position, steps, direction, color)
        print("vertice : ", v.start, v.end, v.shoelace)
        self.vertices.append(v)

    def count(self):
        my_sum = 0
        for v in self.vertices:
            my_sum += v.shoelace
        return my_sum / 2
