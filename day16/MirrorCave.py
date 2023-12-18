from MyMods.Matrix import Matrix
from day16.cavecell import CaveCell


class MirrorCave(Matrix):
    def __init__(self, dimj, dimi):
        super().__init__(dimj, dimi, base=0)
        self.start = 0, 0
        self.crossing = []
        self.consecutive = 0

    def add_lines(self, lines):
        """
           Adds multiple lines lines to the matrix
        """
        for (j, line) in enumerate(lines):
            for i in range(self.dimi):
                c = CaveCell(line[i], (j, i))
                self.grid[j][i] = c

    def walk(self):
        cell = self.grid[self.start[0]][self.start[1]].next_cell()
        while True:
            pass



    def __str__(self):
        """
           Returns a string representation of the matrix
        """
        t = ""
        for j in range(self.dimj):
            for i in range(self.dimi):
                t += str(self.grid[j][i].get_value())
            t += "\n"
        return t
