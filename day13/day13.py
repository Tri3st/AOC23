from MyMods.ReadDataFile import read_data
from day13.mirrors import Mirrors

# fix datalines to grab each mirror
datalines = read_data("day13/input_day13.txt")

datalines2 = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#""".split("\n\n")


def part1():
    print(datalines2)
    # Your code for part 1 goes here
    mirrors = Mirrors(datalines2)
    print(mirrors)
    print(len(mirrors.mirrors))


def part2():
    # Your code for part 2 goes here
    pass
