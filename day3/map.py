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
        self._calc()
        #self.check_numbers()

    def _calc(self):
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
                    num['raw'].append(self.grid[j][i])
                    num['start'] = (j, i)
                    num['length'] += 1
                    if i == (self.dimi - 1) or (self.grid[j][i + 1] in self.symbols):
                        for ind in range(num['length']):
                            num['val'] += int(num['raw'][ind]) * pow(10, num['length'] - ind - 1)
                        self.numbers.append(num)
                        num = {
                            'val': 0,
                            'raw': [],
                            'start': (-1, -1),
                            'length': 0,
                            'has_neighbour': False
                        }

    def check_numbers(self):
        for num in self.numbers:
            result = True
            for i in range(num['length']):
                x = num['start'][0] + i
                y = num['start'][1]
                if i == 0:
                    # start of number
                    if x > 0:
                        if y > 0:
                            result = result and self.grid[y - 1][x] in self.symbols
                            result = result and self.grid[y - 1][x - 1] in self.symbols
                            result = result and self.grid[y][x - 1] in self.symbols
                            result = result and self.grid[y + 1][x - 1] in self.symbols
                            result = result and self.grid[y + 1][x] in self.symbols
                        else:
                            result = result and self.grid[y][x - 1] in self.symbols
                            result = result and self.grid[y + 1][x - 1] in self.symbols
                            result = result and self.grid[y + 1][x] in self.symbols
                    else:
                        if y > 0:
                            result = result and self.grid[y - 1][x] in self.symbols
                            result = result and self.grid[y + 1][x] in self.symbols
                        else:
                            result = result and self.grid[y + 1][x] in self.symbols
                elif i == num['length'] - 1:
                    # end of number
                    if x < self.dimi - 1:
                        if y < self.dimj - 1:
                            result = result and self.grid[y - 1][x] in self.symbols
                            result = result and self.grid[y - 1][x + 1] in self.symbols
                            result = result and self.grid[y][x + 1] in self.symbols
                            result = result and self.grid[y + 1][x + 1] in self.symbols
                            result = result and self.grid[y + 1][x] in self.symbols
                        else:
                            result = result and self.grid[y][x + 1] in self.symbols
                            result = result and self.grid[y - 1][x + 1] in self.symbols
                            result = result and self.grid[y - 1][x] in self.symbols
                    else:
                        if y < self.dimj - 1:
                            result = result and self.grid[y - 1][x] in self.symbols
                            result = result and self.grid[y + 1][x] in self.symbols
                        else:
                            result = result and self.grid[y - 1][x] in self.symbols
                else:
                    # middle of number
                    if y == 0:
                        result = result and self.grid[y + 1][x] in self.symbols
                    elif y == self.dimj - 1:
                        result = result and self.grid[y - 1][x] in self.symbols
                    else:
                        print(i, x, y)
                        result = result and self.grid[y - 1][x] in self.symbols
                        result = result and self.grid[y + 1][x] in self.symbols
                num['has_neighbour'] = result
                result = True

    def __str__(self):
        return super().__str__()
