from MyMods.Matrix import Matrix


class Map(Matrix):
    def __init__(self, dimj, dimi):
        super().__init__(dimj, dimi)
        self.numbers = []
        self.symbols = ['*', '$', '+', '#', '.', '=', '/', '@', '%', '&', '-']

    def add_lines(self, lines):
        for (j, line) in enumerate(lines):
            for i in range(self.dimi):
                self.grid[j][i] = line[i]

    def calc(self):
        num = {
            'val': 0,
            'raw': [],
            'start': (-1, -1),
            'length': 0,
            'has_neighbour': False
        }
        for j in range(self.dimj):
            for i in range(self.dimi):
                if self.grid[j][i] not in self.symbols:
                    num['raw'] += (self.grid[j][i] * pow(10, num['length']))
                    num['start'] = (j, i)
                    num['length'] += 1
                    if i == (self.dimi - 1) or self.grid[j][i + 1] in self.symbols:
                        self.numbers.append(num)
                        num = {
                            'val': 0,
                            'raw': [],
                            'start': (-1, -1),
                            'length': 0,
                            'has_neighbour': False
                        }

    def check_number(self, number):
        pass

    def __str__(self):
        return super().__str__()
