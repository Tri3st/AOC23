from MyMods.ReadDataFile import read_data
from day6.races import Races

datalines = read_data("day6/input_day6.txt", mode=1)

datalines2 = """Time:      7  15   30
Distance:  9  40  200"""


def part1():
    # Your code for part 1 goes here
    races = Races(datalines)
    races.race()
    print(races)
    print("wins : ", races.wins)
    print("solution : ", races.get_solution())


def part2():
    races = Races(datalines, part_two=True)
    races.race()
    print(races)
    print("wins : ", races.wins)
    print("solution : ", races.get_solution())
