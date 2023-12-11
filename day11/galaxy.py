from MyMods.Matrix import Matrix


class Galaxy(Matrix):
    def __init__(self, dimj, dimi):
        super().__init__(dimj, dimi, base='.')
        self.galaxies = []
        self.distances = []
        self.distances2 = []
        self.empty_rows = []
        self.empty_cols = []

    def add_lines(self, lines):
        super().add_lines(lines)

    def expand(self):
        self.dimj += len(self.empty_rows)
        self.dimi += len(self.empty_cols)

        # for each empty row add extra row
        for j in range(self.dimj - 1, -1, -1):
            if j in self.empty_rows:
                self.grid.insert(j, ['.'] * self.dimi)

        # for each empty column add extra column
        for i in range(self.dimi - 1, -1, -1):
            if i in self.empty_cols:
                for j in range(self.dimj):
                    self.grid[j].insert(i, '.')

    def get_empty_rows_cols(self):
        # check rows for no galaxies
        for j in range(self.dimj):
            empty = [i for i in range(self.dimi) if self.grid[j][i] == '.']
            if len(empty) == self.dimi:
                self.empty_rows.append(j)

        # check columns for no galaxies
        for i in range(self.dimi):
            empty = [j for j in range(self.dimj) if self.grid[j][i] == '.']
            if len(empty) == self.dimj:
                self.empty_cols.append(i)

    def calc_distance(self, g1, g2, mult=1):
        distance = (abs(g1[1][0] - g2[1][0]) + abs(g1[1][1] - g2[1][1]))
        for j in range(g1[1][0], g2[1][0] + 1):
            if j in self.empty_rows:
                distance += mult - 1
        for i in range(g1[1][1], g2[1][1] + 1):
            if i in self.empty_cols:
                distance += mult - 1
        return distance

    def find_galaxies(self):
        x = 0
        for j in range(self.dimj):
            for i in range(self.dimi):
                if self.grid[j][i] == '#':
                    self.galaxies.append((x, (j, i)))
                    x += 1
        self.get_empty_rows_cols()

    def calc_distance2(self, g1, g2, mult=1):
        print(self.empty_cols, self.empty_rows)
        rows = [j for j in range(g1[1][0], g2[1][0] + 1)] if g1[1][0] < g2[1][0] else \
            [j for j in range(g2[1][0], g1[1][0] + 1)]
        cols = [i for i in range(g1[1][1], g2[1][1] + 1)] if g1[1][1] < g2[1][1] else \
            [i for i in range(g2[1][1], g1[1][1] + 1)]
        print(cols, rows)
        distance = (len(rows) - 1) + (len(cols) - 1)
        print("distance before : ", distance)
        rows = rows[1:-1]
        if rows:
            for c1 in rows:
                if c1 in self.empty_rows:
                    distance += (mult - 1)
        cols = cols[1:-1]
        if cols:
            for c2 in cols:
                if c2 in self.empty_cols:
                    distance += (mult - 1)
        print(cols, rows)
        print("distance after : ", distance)
        return distance

    def find_distances(self):
        for index, g in enumerate(self.galaxies):
            for f in self.galaxies[index + 1:]:
                self.distances.append((g[0], f[0], abs(g[1][0] - f[1][0]) + abs(g[1][1] - f[1][1])))

    def find_distances_part_2(self, multpl=1):
        print("multiplier = : ", multpl)
        for d in self.distances:
            self.distances2.append((d[0], d[1], self.calc_distance2(self.galaxies[d[0]], self.galaxies[d[1]], multpl)))

    def get_total_distance(self):
        return sum([d[2] for d in self.distances])

    def get_total_distance_part_2(self):
        return sum([d[2] for d in self.distances2])
