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
    # m1 = Map(len(datalines2), len(datalines2[0]))
    # m1.add_lines(datalines2)
    # print(m1)
    # print("Sum of parts : ", m1.get_part_sum())
    #
    # for the big one :
    m = Map(len(datalines), len(datalines[0]))
    m.add_lines(datalines)
    print("Sum of the parts : ", m.get_part_sum())


def part2():
    # Your code for part 2 goes here
    #
    # First the small one :
    # m1 = Map(len(datalines2), len(datalines2[0]))
    # m1.add_lines(datalines2)
    #
    # now the big one :
    m1 = Map(len(datalines), len(datalines[0]))
    m1.add_lines(datalines)
    print(m1)
    ratios = m1.gear_ratios()
    print("Gear ratios : ", ratios)
    sum_of_products = 0
    for ratio in ratios:
        print("Gear ratio : ", ratio)
        rs = [r for r in ratio]
        sum_of_products += (rs[0] * rs[1])
    print("Sum of products : ", sum_of_products)
