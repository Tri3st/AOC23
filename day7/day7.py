from MyMods.ReadDataFile import read_data
from day7.game import Game

datalines = read_data("day7/input_day7.txt")

datalines2 = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".split("\n")


def part1():
    # Your code for part 1 goes here
    game = Game(datalines2)
    print(game)
    game.get_rankings()
    print(game.ranking)


def part2():
    # Your code for part 2 goes here
    pass
