import re

from MyMods.Matrix import Matrix
from day18.dig import Dig


class Lagoon(Matrix):
    def __init__(self):
        super().__init__(1000, 1000)
        self.directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        self.current_position = (500, 200)
        self.add_lines2()

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

    def count(self):
        count = 0
        inside = False
        for j in range(self.dimj):
            for i in range(self.dimi):
                if self.grid[j][i].value == '#':
                    count += 1
                    if self.grid[j][i+1] == '#':
                        pass
                    else:
                        inside = not inside
                elif inside:
                    count += 1
        return count
