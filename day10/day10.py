from MyMods.ReadDataFile import read_data
from day10.PipeMap import PipeMap

datalines = read_data("day10/input_day10.txt")

datalines2 = """.....
.S-7.
.|.|.
.L-J.
.....""".split("\n")


def part1():
    # Your code for part 1 goes here
    pipe = PipeMap(len(datalines2), len(datalines2[0]))
    pipe.add_lines(datalines2)
    print(pipe)
    pipe.get_start()

def part2():
    # Your code for part 2 goes here
    pass
