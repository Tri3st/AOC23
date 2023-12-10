from MyMods.ReadDataFile import read_data
from day9.series import Series

datalines = read_data("day9/input_day9.txt")

datalines2 = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""".split("\n")


def part1():
    # Your code for part 1 goes here
    test = "1 3 6 10 15 21"
    series = Series(test)
    print(series)
    series.calc_next()
    print(series)


def part2():
    # Your code for part 2 goes here
    pass
