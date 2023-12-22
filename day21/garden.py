from MyMods.Matrix import Matrix


class Garden(Matrix):
    def __init__(self, dimj, dimi):
        super().__init__(dimj, dimi, base=".")
        self.start = self.find_start()
        self.next_step = None
        self.steps = 0
        while True:
            neighbors = None
            self.next_step = self.find_poss_neigbors(self.start[0], self.start[1])
            for n in self.next_step:
                neighbors = self.find_poss_neigbors(n[0], n[1])
                self.steps += 1
                if neighbors:
                    pass

    def find_start(self):
        for j in range(self.dimj):
            for i in range(self.dimi):
                if self.grid[j][i] == "S":
                    return j, i
        return None

    def find_poss_neigbors(self, j, i):
        poss_neigbors = []
        if j > 0:
            poss_neigbors.append((j - 1, i))
        if j < self.dimj - 1:
            poss_neigbors.append((j + 1, i))
        if i > 0:
            poss_neigbors.append((j, i - 1))
        if i < self.dimi - 1:
            poss_neigbors.append((j, i + 1))
        for neighbor in poss_neigbors:
            if self.grid[neighbor[0]][neighbor[1]] == "#":
                poss_neigbors.remove(neighbor)
        return poss_neigbors
