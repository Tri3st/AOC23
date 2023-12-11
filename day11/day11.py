from MyMods.ReadDataFile import read_data
from day11.galaxy import Galaxy

datalines = read_data("day11/input_day11.txt")

datalines2 = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""".split("\n")


def part1():
    # Your code for part 1 goes here
    g = Galaxy(len(datalines), len(datalines[0]))
    g.add_lines(datalines)
    g.expand()
    g.find_galaxies()
    g.find_distances()
    print("distances : ", g.distances, " ", len(g.distances), " distances")
    print("total distance : ", g.get_total_distance())
    print(g)


def part2():
    # Your code for part 2 goes here
    g = Galaxy(len(datalines), len(datalines[0]))
    g.add_lines(datalines)
    g.find_galaxies()

    g.find_distances()

    g.find_distances_part_2(1000000)

    print("total distance 2 : ", g.get_total_distance_part_2())
