from MyMods.Matrix import Matrix


class Mirror(Matrix):
    def __init__(self, datalines):
        super().__init__(len(datalines), len(datalines[0]), base='.')
        self.add_lines(datalines)

    def detect_vertical_reflection(self):
        for refl_line in range()



    def detect_horizontal_reflection(self):
        pass
