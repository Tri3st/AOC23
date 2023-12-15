import re


class WordCode:
    def __init__(self, word):
        pattern = r"""^(?P<label>[a-z]+)(?P<sign>[=-])(?P<strength>[0-9]*)$"""
        groups = re.findall(pattern, word)[0]
        self.label = groups[0]
        self.sign = groups[1]
        self.strength = int(groups[2]) if groups[1] == "=" else None
        self.word = word
        self.hash = self.calc(self.word)
        self.small_hash = self.calc(self.label)

    def calc(self, word):
        res = 0
        for x in word:
            res += ord(x)
            res *= 17
            res = res % 256
        return res

    def get_hash(self):
        return self.hash

    def get_small_hash(self):
        return self.small_hash

    def get_sign(self):
        return self.sign

    def get_strength(self):
        return self.strength

    def get_label(self):
        return self.label

    def is_label(self, label):
        return self.label == label

    def __str__(self):
        return f"{self.label} - {self.strength}"
