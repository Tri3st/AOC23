import re

from MyMods.Matrix import Matrix
from day18.dig import Dig


class Lagoon(Matrix):
    def __init__(self):
        super().__init__(100, 100)
        self.directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        self.current_position = (50, 20)
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

    def not_the_last_one(self, j, i):
        for x in range(i + 1, self.dimi):
            if self.grid[j][x].value == '#':
                return True
        return False

    def count(self):
        count = 0
        inside = False
        for j in range(self.dimj):
            for i in range(self.dimi):
                # count the #'s in a row
                if self.grid[j][i].value == '#':
                    if self.grid[j][i+1] == '#':
                        c = 0
                        while True:
                            if self.grid[j][i + c].value == '#':
                                count += 1
                                c += 1
                            else:
                                i = i + c
                                break
                    # count all spaces until the next one, but NOT if it is the last one
                    elif self.not_the_last_one(j, i):
                        # count all spaces till next one
                        d = 0
                        while True:
                            if self.grid[j][i + d].value == '.':
                                self.grid[j][i + d].value = 'x'
                                count += 1
                                d += 1
                            else:
                                i = i + d
                                break
        return count
