import re


class LavaCode:
    def __init__(self, data):
        data = data.split(" ")
        self.springs = data[0].split()
        self.groups = [ int(x) for x in data[1].split(",")]
        self.count_damaged()

    def count_damaged(self):
        match = r".(#+)."
        pattern = r".?([?#]+).?"
        test = re.findall(pattern, self.springs[0])
        print(test)

    def __str__(self):
        return "Springs: {}\nGroups: {}".format(self.springs, self.groups)