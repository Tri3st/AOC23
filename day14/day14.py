from MyMods.ReadDataFile import read_data
from day14.Cave import Cave

datalines = read_data("day14/input_day14.txt")

datalines2 = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""".split("\n")


def part1():
    # Your code for part 1 goes here
    cave = Cave(datalines)
    print(cave)
    cave.tilt()
    print(cave.boulders)
    print(cave.calc_weight_part(4, 6))
    print(cave.calc_weights())


def part2():
    # Your code for part 2 goes here
    pass
