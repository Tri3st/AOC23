from MyMods.Matrix import Matrix


class Cave(Matrix):
    def __init__(self, datalines):
        super().__init__(len(datalines), len(datalines[0]), base='.')
        self.add_lines(datalines)
        self.boulders = []
        self.weights = {0: 0}

    def tilt(self):
        b = {
            'id': 0,
            'col': -1,
            'count': 0,
            'next_hash': None
        }
        for col in range(self.dimi):
            # count O in column til next #
            b['col'] = col
            for row in range(self.dimj):
                if self.grid[row][col] == 'O':
                    b['count'] += 1
                if self.grid[row][col] == '#':
                    b['next_hash'] = row
                    b['id'] += 1
                    self.boulders.append(b)
                    b = {
                        'id': b['id'],
                        'col': col,
                        'count': 0,
                        'next_hash': None
                    }
                if row == self.dimj - 1:
                    self.boulders.append(b)
                    b = {
                        'id': b['id'] + 1,
                        'col': col + 1,
                        'count': 0,
                        'next_hash': None
                    }

    def calc_weight_part(self, min1, max1):
        # fill weights
        weight = 0
        for i in range(max1 - min1 + 1):
            weight += self.dimj - (min1 + i)
        return weight

    def calc_weights(self, start_hash=0):
        ws = []
        for c in range(self.dimi):
            # group per column
            column = [b for b in self.boulders if b['col'] == c]
            print(column)
            nexth = 0
            for cl in column:
                if cl['next_hash'] is None:
                    if cl['count'] > 0:
                        ws.append(self.calc_weight_part(nexth, nexth + cl['count'] - 1))
                    break
                else:
                    if cl['count'] > 0:
                        ws.append(self.calc_weight_part(nexth, nexth + cl['count'] - 1))
                    nexth = cl['next_hash'] + 1

        print(ws)
        return sum(ws)