from MyMods.ReadDataFile import read_data
from day21.garden import Garden

datalines = read_data("day21/input_day21.txt")

datalines2 = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........""".split("\n")


def part1():
    # Your code for part 1 goes here
    garden = Garden(len(datalines2), len(datalines2[0]), datalines2)
    print(garden)



def part2():
    # Your code for part 2 goes here
    pass
