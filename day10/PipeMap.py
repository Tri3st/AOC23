from MyMods.Matrix import Matrix
from day10.pipe import Pipe


class PipeMap(Matrix):
    def __init__(self, dimj, dimi):
        super().__init__(dimj, dimi, base=".")
        self.start = None

    def get_start(self):
        for j in range(self.dimj):
            for i in range(self.dimi):
                if self.grid[i][j].value == 'S':
                    return self.grid[i][j]

    def add_lines(self, lines):
        for j in range(self.dimj):
            for i in range(self.dimi):
                self.grid[j][i] = Pipe(lines[j][i], (j, i))

    def __str__(self):
        res = ""
        for j in range(self.dimj):
            for i in range(self.dimi):
                res += str(self.grid[j][i])
            res += "\n"
        return res

