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
        self.prev = None
        self.next = None
        self.distance = 0

    def __str__(self):
        return f"{self.value} "
