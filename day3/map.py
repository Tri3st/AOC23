from MyMods.Matrix import Matrix


class Map(Matrix):
    def __init__(self, dimj, dimi):
        super().__init__(dimj, dimi)
        self.numbers = []
        self.symbols = ['*', '$', '+', '#', '.', '=', '/', '@', '%', '&', '-']

    def calc(self):
        nums = []
        for j in range(self.dimj):
            num = {
                'value': [],
                'start': [],
                'length': 0,
            }
            for i in range(self.dimi):
                if self.grid[j][i].isnumeric():
                    num['value'].append(self.grid[j][i])
                    num['start'] = [j, i] if not num['start'] else num['start']
                    num['length'] += 1
                    if not self.grid[j][i+1].isnumeric():
                        nums.append(num)
                        num = {
                            'value': [],
                            'start': [],
                            'length': 0,
                        }
        print(nums)
        self.numbers = nums

    def check_number(self, number):
        result = True
        for i in range(number['length']):
            x = number['start'][0] + i
            y = number['start'][1]
            if i == 0:
                # beginning of number
                print("beginning of number (%d, %d) and i is  %d" % (x, y, i))
                if y > 0 and self.grid[y-1][x] in self.symbols:
                    result = result and False
                elif x > 0:
                    if self.grid[y][x - 1] in self.symbols:
                        result = result and False
                    elif y > 0 and self.grid[y-1][x - 1] in self.symbols:
                        result = result and False
                    elif y < self.dimj-1 and self.grid[y+1][x - 1] in self.symbols:
                        result = result and False
                elif y < self.dimj-1 and self.grid[y+1][x] in self.symbols:
                    result = result and False
            elif i == number['length'] - 1:
                # end of number
                print("end of number (%d, %d) and i is  %d" % (x, y, i))
                if y > 0 and self.grid[y-1][x] in self.symbols:
                    result = result and False
                elif x < self.dimi-1:
                    if self.grid[y][x + 1] in self.symbols:
                        result = result and False
                    elif y > 0 and x < self.dimi and self.grid[y-1][x + 1] in self.symbols:
                        result = result and False
                    elif y < self.dimj - 1 and x < self.dimi - 1 and self.grid[y + 1][x + 1] in self.symbols:
                        result = result and False
                elif y < self.dimj - 1 and self.grid[y + 1][x] in self.symbols:
                    result = result and False
            elif 0 < i < number['length'] - 1:
                # middle of number
                print("middle of number (%d, %d) and i is  %d" % (x, y, i))
                if y > 0 and self.grid[y - 1][x] in self.symbols:
                    result = result and False
                elif y < self.dimj - 1 and self.grid[y + 1][x] in self.symbols:
                    result = result and False
        return result

    def __str__(self):
        return super().__str__()
