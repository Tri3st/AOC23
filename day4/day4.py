from MyMods.ReadDataFile import read_data
from day4.BingoCard import BingoCard

datalines = read_data("day4/input_day4.txt")

datalines2 = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".split("\n")

def part1():
    # Your code for part 1 goes here
    cards = []
    for line in datalines:
        b = BingoCard(line)
        print(b)
        cards.append(b)
    total = sum([c.get_score() for c in cards])
    print("Total : ", total)


def part2():
    # Your code for part 2 goes here
    cards = []
    for line in datalines:
        b = BingoCard(line)
        print(b)
        cards.append(b)

    card_numbers = 0
    for i, sc in enumerate(cards):
        if sc.get_score():


