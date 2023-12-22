from MyMods.Matrix import Matrix


class Garden(Matrix):
    def __init__(self, dimj, dimi, lines):
        super().__init__(dimj, dimi, base=".")
        self.start = None
        self.next_step = None
        self.steps = 0
        self.add_lines(lines)
        self.start = self.find_start()


    def step(self):
        while True:
            neighbors = None
            self.next_step = self.find_poss_neigbors(self.start[0], self.start[1])
            for n in self.next_step:
                neighbors.append(self.find_poss_neigbors(n[0], n[1]))
                neighbors.remove(n)
                self.steps += 1
                if neighbors:
                    pass
                else:
                    break

    def find_start(self):
        for j in range(self.dimj):
            for i in range(self.dimi):
                if self.grid[j][i] == "S":
                    print("Start found at", j, i)
                    return (j, i)
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
