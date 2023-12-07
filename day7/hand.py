"""

    Five of a kind, where all five cards have the same label: AAAAA
    Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    High card, where all cards' labels are distinct: 23456

Hands are primarily ordered based on type; for example, every full house is stronger than any three of a kind.
"""


def count_card(cards):
    result = {}
    for c in cards:
        if c in result.keys():
            result[c] += 1
        else:
            result[c] = 1
    return result


class Hand:
    def __init__(self, hand, bid):
        self.CARDS = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4,
                      '4': 3, '3': 2, '2': 1}
        self.RANKS = {'High Card': 1, 'One Pair': 2, 'Two Pairs': 3, 'Three of a Kind': 4, 'Full House': 5,
                      'Four of a Kind': 6, 'Five of a kind': 7}
        self.cards = []
        self.points = {
            'primary': 0,
            'secondary': 0
        }
        self.highest_card = ''
        self.rank = 0
        for card in hand:
            self.cards.append(card)
        self.bid = bid
        self.calc_points()

    def highest_card_points(self):
        return self.CARDS[self.highest_card]

    def calc_points(self):
        if self.is_five_of_a_kind():
            self.points['primary'] = self.RANKS['Five of a kind']
        elif self.is_four_of_a_kind():
            self.points['primary'] = self.RANKS['Four of a Kind']
        elif self.is_full_house():
            self.points['primary'] = self.RANKS['Full House']
        elif self.is_three_of_a_kind():
            self.points['primary'] = self.RANKS['Three of a Kind']
        elif self.is_two_pair():
            self.points['primary'] = self.RANKS['Two Pairs']
        elif self.is_one_pair():
            self.points['primary'] = self.RANKS['One Pair']
        elif self.is_high_card():
            self.points['primary'] = self.RANKS['High Card']
        else:
            print("huh?!")

    def is_five_of_a_kind(self):
        self.highest_card = self.cards[0]
        return self.cards[0] == self.cards[1] == self.cards[2] == self.cards[3] == self.cards[4]

    def is_four_of_a_kind(self):
        count = count_card(self.cards)
        result = 4 in count.values()
        if result:
            self.highest_card = [k for k, v in count.items() if v == 4][0]
        return result

    def is_full_house(self):
        count = count_card(self.cards)
        result = 3 in count.values() and 2 in count.values()
        if result:
            self.highest_card = [k for k, v in count.items() if v == 3][0]
        return result

    def is_three_of_a_kind(self):
        count = count_card(self.cards)
        result = 3 in count.values()
        if result:
            self.highest_card = [k for k, v in count.items() if v == 3][0]
        return result

    def is_two_pair(self):
        count = count_card(self.cards)
        result = len([k for k, v in count.items() if v == 2]) == 2
        if result:
            self.highest_card = max([k for k, v in count.items() if v == 2])
        return result

    def is_one_pair(self):
        count = count_card(self.cards)
        result = len([k for k, v in count.items() if v == 2]) == 1
        if result:
            self.highest_card = [k for k, v in count.items() if v == 2][0]
        return result

    def is_high_card(self):
        count = count_card(self.cards)
        result = len([k for k, v in count.items() if v == 1]) == 5
        if result:
            self.highest_card = max(k for k, v in count.items())
        return result

    def __str__(self):
        result = f"Hand: "
        for card in self.cards:
            result += f"{card} "
        result += f" bid : {self.bid} highest score : {self.points['primary']} ({self.highest_card_points()})\n"
        return result
