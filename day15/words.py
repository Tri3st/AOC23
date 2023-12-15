from day15.wordcode import WordCode


class Words:
    def __init__(self, words):
        self.words = []
        self.hashes = []
        self.hash_value = 0
        for word in words:
            w = WordCode(word)
            self.words.append(w)

    def get_sum(self):
        return sum([d.get_hash() for d in self.words])

    def __str__(self):
        return f"{self.words} - {self.hash_value}"