import re
from day2.cube import Cube


class Grab:
    def __init__(self, cubes):
        self.cubes = []
        pattern = r"\s?(\d+) (\w+),?"
        colors = re.findall(pattern, cubes)
        for color in colors:
            c = Cube(color[1], int(color[0]))
            self.cubes.append(c)

    def get_amount(self, color) -> int:
        for cube in self.cubes:
            if cube.color == color:
                return cube.amount
        return 0

    def __str__(self):
        return f"{self.cubes}"
