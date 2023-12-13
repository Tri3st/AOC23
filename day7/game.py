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

    def __str__(self):
        result = f"Game with {len(self.hands)} hands: \n"
        for hand in self.hands:
            result += f"{hand}\n"
        return result
