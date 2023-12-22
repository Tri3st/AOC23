from MyMods.ReadDataFile import read_data
from day18.calc2 import Calc2
from day18.lagoon import Lagoon

datalines = read_data("day18/input_day18.txt")

datalines2 = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)""".split("\n")

    
def part1():
    # Your code for part 1 goes here
    lagoon = Calc2()
    for line in datalines:
        lagoon.add_operator(line)
    print("area : ", lagoon.count_area())
    print("inner boundry points : ", lagoon.calc_inner_boundry_points())
    print("outer boundry points : ", lagoon.outer_boundry_points)
    print("total : ", lagoon.total())


def part2():
    # Your code for part 2 goes here
    lagoon = Calc2()
    for line in datalines:
        lagoon.add_operator(line, mode=1)
    print("area : ", lagoon.count_area())
    print("inner boundry points : ", lagoon.calc_inner_boundry_points())
    print("outer boundry points : ", lagoon.outer_boundry_points)
    print("total : ", lagoon.total())