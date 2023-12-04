from MyMods.ReadDataFile import read_data
from day3.map import Map

datalines = read_data("day3/input_day3.txt")

datalines2 = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".split("\n")

    
def part1():
    # Your code for part 1 goes here
    m1 = Map(len(datalines2), len(datalines2[0]))
    m1.add_lines(datalines2)
    m1.calc()
    print(m1)
    for number in m1.numbers:
        print(number, m1.check_number(number))


def part2():
    # Your code for part 2 goes here
    pass
