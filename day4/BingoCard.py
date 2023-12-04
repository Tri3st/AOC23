import re


class BingoCard:
    def __init__(self, dataline):
        self.score = None
        pattern1 = r"^Card\s+(\d+):.*$"
        pattern2 = r"\b(\d+)\b"
        nr = re.findall(pattern1, dataline)
        self.card_nr = int(nr[0])
        nums = re.findall(pattern2, dataline)
        all_numbers = [int(x) for x in nums]
        self.winning_numbers = all_numbers[1:6] # [1:11]
        self.my_numbers = all_numbers[6:] # [11:]
        self._calc_score()

    def _calc_score(self):
        matches = []
        for number in self.my_numbers:
            if number in self.winning_numbers:
                matches.append(number)
        if len(matches) > 0:
            self.score = pow(2,len(matches) - 1)
        else:
            self.score = 0

    def get_score(self) -> int :
        return self.score

    def __str__(self):
        my_numbers = " ".join([str(s) for s in self.my_numbers])
        winning_numbers = " ".join([str(s2) for s2 in self.winning_numbers])
        return f"Card {self.card_nr}: {my_numbers} | {winning_numbers} -> score is {self.score}"
