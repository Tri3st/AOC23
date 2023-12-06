from MyMods.Matrix import Matrix


class Map(Matrix):
    def __init__(self, dimj, dimi):
        super().__init__(dimj, dimi)
        self.numbers = []
        self.symbols = ['*', '$', '+', '#', '=', '/', '@', '%', '&', '-', '.']

    def add_lines(self, lines):
        for (j, line) in enumerate(lines):
            for i in range(self.dimi):
                self.grid[j][i] = line[i]
        self._calc()
        self.check_numbers()

    def get_neighbors(self, row: int, col: int):
        neighbors = []
        row_max = self.dimj - 1
        col_max = self.dimi - 1
        neighbors = []
        if row > 0:
            neighbors.append((row - 1, col))
            if col > 0:
                neighbors.append((row - 1, col - 1)) if (row - 1, col - 1) not in neighbors else None
            if col < col_max:
                neighbors.append((row - 1, col + 1)) if (row - 1, col + 1) not in neighbors else None
        if row < row_max:
            neighbors.append((row + 1, col))
            if col > 0:
                neighbors.append((row + 1, col - 1)) if (row + 1, col - 1) not in neighbors else None
            if col < col_max:
                neighbors.append((row + 1, col + 1)) if (row + 1, col + 1) not in neighbors else None
        if col > 0:
            neighbors.append((row, col - 1))
            if row > 0:
                neighbors.append((row - 1, col - 1)) if (row - 1, col - 1) not in neighbors else None
            if row < row_max:
                neighbors.append((row + 1, col - 1)) if (row + 1, col - 1) not in neighbors else None
        if col < col_max:
            neighbors.append((row, col + 1))
            if row > 0:
                neighbors.append((row - 1, col + 1)) if (row - 1, col + 1) not in neighbors else None
            if row < row_max:
                neighbors.append((row + 1, col + 1)) if (row + 1, col + 1) not in neighbors else None
        return neighbors

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
                    num['start'] = (j, i) if num['start'] == (-1, -1) else num['start']
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

    def is_number(self, row: int, col: int) -> int:
        for number in self.numbers:
            coords = [(number['start'][0], number['start'][1] + c) for c in range(number['length'])]
            if (row, col) in coords:
                return number['val']
        return -1

    def check_numbers(self):
        good_numbers = []
        for number in self.numbers:
            # get the neigbors for each number and put these in a set.
            # remove the number coords themselves from the set
            # check the coords if there is a symbol in the set
            coords = [(number['start'][0], number['start'][1] + c) for c in range(number['length'])]
            clean_neighbors = set()
            neighbors = [self.get_neighbors(cds[0], cds[1]) for cds in coords]
            for neighbor in neighbors:
                for n in neighbor:
                    if n not in coords:
                        clean_neighbors.add(n)
            for x in clean_neighbors:
                if self.grid[x[0]][x[1]] in self.symbols and self.grid[x[0]][x[1]] != '.':
                    number['has_neighbour'] = True

    def get_part_sum(self):
        total_sum = 0
        for number in self.numbers:
            if number['has_neighbour']:
                total_sum += number['val']
        return total_sum

    def gear_ratios(self):
        gear_ratios = []
        for j in range(self.dimj):
            for i in range(self.dimi):
                if self.grid[j][i] == '*':
                    gears = set()
                    neighbors = self.get_neighbors(j, i)
                    for neighbor in neighbors:
                        # check if a neighbour is a number
                        # if we have 2 different numbers as neighbours, we have a gear ratio
                        gear = self.is_number(neighbor[0], neighbor[1])
                        if gear != -1:
                            print("add gear ", gear)
                            gears.add(gear)
                    print(gears)
                    if len(gears) == 2:
                        gear_ratios.append(gears)
                        print(gears)
        return gear_ratios

    def __str__(self):
        return super().__str__()
