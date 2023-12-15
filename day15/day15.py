from MyMods.ReadDataFile import read_data
from day15.boxes import Boxes
from day15.words import Words

datalines = read_data("day15/input_day15.txt", mode=1).split(",")

datalines2 = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7""".split(",")

    
def part1():
    # Your code for part 1 goes here
    words = Words(datalines2)
    print(words.words)
    for word in words.words:
        print(word)
    print(words.get_sum())


def part2():
    # Your code for part 2 goes here
    words = Words(datalines)
    boxes = Boxes()
    for word in words.words:
        boxes.add(word)

    print(boxes)
    print(boxes.calc_focusing_power())

