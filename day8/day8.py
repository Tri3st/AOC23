from MyMods.ReadDataFile import read_data
from day8.instructions import Instructions

datalines = read_data("day8/input_day8.txt")

datalines2 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)""".split("\n")

datalines3 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)""".split("\n")

datalines4 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)""".split("\n")


def part1():
    # Your code for part 1 goes here
    instructions = Instructions(datalines)
    instructions.traverse()


def part2():
    # Your code for part 2 goes here
    instructions = Instructions(datalines)
    instructions.multi_traverse()

