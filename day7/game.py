from day7.hand import Hand


class Game:
    def __init__(self, data):
        self.hands = []
        self.total_winnings = 0
        self.ranking = {}
        for line in data:
            line2 = line.split(" ")
            self.hands.append(Hand(line2[0], int(line2[1])))

    def get_rankings(self):
        self.hands.sort(key=lambda x: x.points['primary'], reverse=False)
        rank = 1
        highest_score = 1
        for i in range(len(self.hands)):
            hands_in_group = [x for x in self.hands if x.points['primary'] == highest_score]
            if len(hands_in_group) > 1:
                hands_in_group.sort(key=lambda x: x.highest_card_points(), reverse=True)
                for hand2 in hands_in_group:
                    print("inside loop : ", hand2)
                    self.ranking[rank] = rank * hand2.bid
                rank += 1
            else:
                self.ranking[rank] = rank * self.hands[i].bid
                rank += 1
            highest_score += 1

    def __str__(self):
        result = f"Game with {len(self.hands)} hands: \n"
        for hand in self.hands:
            result += f"{hand}\n"
        return result
