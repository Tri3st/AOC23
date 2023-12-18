from MyMods.ReadDataFile import read_data
from day16.MirrorCave import MirrorCave

datalines = read_data("day16/input_day16.txt")
# get the slashed first ... \\ -> *

datalines2 = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....""".replace('\\', '*').split("\n")

    
def part1():
    # Your code for part 1 goes here
    print(datalines2)
    mirror = MirrorCave(len(datalines2), len(datalines2[0]))
    mirror.add_lines(datalines2)
    print(mirror)


def part2():
    # Your code for part 2 goes here
    pass
