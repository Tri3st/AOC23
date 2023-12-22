import re

from day18.vertices import Vertices


class Calc2:
    def __init__(self):
        self.directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        self.current_position = (0, 0)
        self.inner_boundry_points = 0
        self.outer_boundry_points = 0
        self.vertices = []
        self.coords = []

    def add_operator(self, dataline, mode=0):
        pattern = r"^(?P<direction>[UDLR]) (?P<steps>\d+) \(#(?P<color>[0-9a-f]{6})\)$"
        matches = re.findall(pattern, dataline)[0]
        direction = matches[0][0]
        steps = int(matches[1])
        color = matches[2]
        if mode == 1:
            steps2, direction2 = self.convert_rgb(color)
            self.do_operation(direction2, steps2, color)
        else:
            self.do_operation(direction, steps, color)

    def do_operation(self, direction, steps, color):
        x, y = self.current_position
        self.coords.append(self.current_position)
        end = None
        if direction == 'U':
            self.current_position = (x, steps + y)
        elif direction == 'D':
            self.current_position = (x, y - steps)
        elif direction == 'L':
            self.current_position = (x - steps, y)
        elif direction == 'R':
            self.current_position = (x + steps, y)
        v = Vertices((x, y), self.current_position, steps, direction, color)
        print("vertice : ", v.start, v.end, v.shoelace)
        self.outer_boundry_points += steps
        self.vertices.append(v)

    def count_area(self):
        my_sum = 0
        for v in self.vertices:
            my_sum += v.shoelace
        return abs(my_sum) / 2

    def calc_inner_boundry_points(self):
        temp = self.count_area() - (self.outer_boundry_points / 2) + 1
        self.inner_boundry_points = int(temp)
        return temp

    def total(self):
        return self.inner_boundry_points + self.outer_boundry_points

    def convert_rgb(self, color):
        DIRECTIONS = {0: 'R', 1: 'D', 2: 'L', 3: 'U'}
        dist = int(color[0:5], 16)
        direction = DIRECTIONS[int(color[5])]
        return dist, direction
