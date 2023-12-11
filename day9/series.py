from day9.serie import Serie


class Series:
    def __init__(self, data):
        self.series = []
        self.series.append(Serie(data))
        self.index = 0
        while True:
            if self.series[self.index].all_zeroes():
                break
            else:
                result = self.series[self.index].return_diffs()
                self.series.append(Serie(result))
                self.index += 1

    def calc_next(self):
        i = len(self.series) - 1
        s = self.series[i]
        s.add_num(0)
        while True:
            i -= 1
            s = self.series[i]
            s_current = self.series[i + 1]
            s.add_num(s_current.return_last() + s.return_last())
            if i == 0:
                break

    def calc_previous(self):
        i = len(self.series) - 1
        s = self.series[i]
        s.add_num_front(0)
        while True:
            i -= 1
            s = self.series[i]
            s_current = self.series[i + 1]
            s.add_num_front(s.return_first() - s_current.return_first())
            if i == 0:
                break

    def get_solution(self):
        return self.series[0].return_last()

    def get_solution_part_2(self):
        return self.series[0].return_first()

    def __str__(self):
        res = ""
        for i in range(len(self.series)):
            res += (" " * 2 * i) + f"{self.series[i]}\n"
        return res
