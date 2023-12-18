class Dig:
    def __init__(self, coords):
        self.value = "."
        self.colors = []
        self.coords = coords

    def add_color(self, color):
        self.value = "#"
        if color not in self.colors:
            self.colors.append(color)

    def __str__(self):
        return self.value
