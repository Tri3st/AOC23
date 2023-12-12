from MyMods.ReadDataFile import read_data
from day10.PipeMap import PipeMap

datalines = read_data("day10/input_day10.txt")

datalines2 = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ""".split("\n")


def part1():
    # Your code for part 1 goes here
    pipe = PipeMap(len(datalines2), len(datalines2[0]))
    pipe.add_lines(datalines2)
    print(pipe)
    pipe.get_start()
    print(pipe.start)
    pipe.walk()


def part2():
    # Your code for part 2 goes here
    pass
