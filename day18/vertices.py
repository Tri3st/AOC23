class Vertices:
    def __init__(self, start, end, length, direction, color):
        self.start = start
        self.end = end
        self.length = length
        self.direction = direction
        self.color = color
        self.shoelace = self.calculate()

    def calculate(self):
        x, y = self.start
        x2, y2 = self.end
        return (x * y2) - (y * x2)