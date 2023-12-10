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
        print(self.series)

    def calc_next(self):
        i = len(self.series) - 1
        s = self.series[i]
        for i in range(len(self.series) - 1, -1, -1):
            print(self.series[i])
            nums = self.series[i].return_last_two()
            print(nums)
            self.series[i].add_num(self.series[i].return_last() + (nums[1] - nums[0]))

    def __str__(self):
        res = ""
        for i in range(len(self.series)):
            res += (" " * 2 * i) + f"{self.series[i]}\n"
        return res
