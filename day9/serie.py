class Serie:
    def __init__(self, data):
        print(data)
        self.serie = [int(x) for x in data.strip().split(" ")]
        self.length = len(self.serie)

    def all_zeroes(self):
        l1 = [s for s in self.serie if s == 0]
        return len(l1) == len(self.serie)

    def all_nums(self):
        for i in range(len(self.serie) - 1):
            if self.serie[i] != self.serie[i + 1]:
                return -1
        return self.serie[0]

    def return_diffs(self):
        res = ""
        for i in range(len(self.serie) - 1):
            res += f"{self.serie[i + 1] - self.serie[i]} "
        return res

    def return_last(self):
        return self.serie[-1]

    def return_last_two(self):
        return self.serie[-2], self.serie[-1]

    def add_num(self, num):
        self.serie.append(num)

    def __str__(self):
        return "   ".join([str(x) for x in self.serie])

