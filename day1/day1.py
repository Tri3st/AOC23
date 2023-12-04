from MyMods.ReadDataFile import read_data
        
datalines = read_data("day1/input_day1.txt")

datalines2 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".split("\n")

written_numbers = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"
]
written_numbers_2 = {
    "one": {
        "num": 1,
        "start": "o",
        "len": 3
    },
    "two": {
        "num": 2,
        "start": "t",
        "len": 3
    },
    "three": {
        "num": 3,
        "start": "t",
        "len": 5
    },
    "four": {
        "num": 4,
        "start": "f",
        "len": 4
    },
    "five": {
        "num": 5,
        "start": "f",
        "len": 4
    },
    "six": {
        "num": 6,
        "start": "s",
        "len": 3
    },
    "seven": {
        "num": 7,
        "start": "s",
        "len": 5
    },
    "eight": {
        "num": 8,
        "start": "e",
        "len": 5
    },
    "nine": {
        "num": 9,
        "start": "n",
        "len": 4
    },
    "zero": {
        "num": 0,
        "start": "z",
        "len": 4
    }
}

written_numbers_start_letters = [
    "o", "t", "f", "s", "e", "n", "z"
]

datalines3 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".split("\n")


def get_number(line):
    number = []
    for char in line:
        if char.isdigit():
            number.append(int(char))
    if len(number) == 1:
        return number[0] * 10 + number[0]
    else:
        return number[0] * 10 + number[-1]


def get_number_part2(line):
    number = []
    for (index, char) in enumerate(line):
        if char.isdigit():
            number.append(int(char))
        elif char.isalpha():
            for num in written_numbers_2:
                if char == written_numbers_2[num]['start']:
                    if line[index:index + written_numbers_2[num]['len']] == num:
                        number.append(written_numbers_2[num]['num'])
    if len(number) == 1:
        return number[0] * 10 + number[0]
    else:
        return number[0] * 10 + number[-1]


def part1():
    # Your code for part 1 goes here
    result = 0
    for line in datalines:
        x = get_number_part2(line)
        result += x
        print(line, x, result)
    print(result)


def part2():
    # Your code for part 2 goes here
    result = 0
    for line in datalines:
        x = get_number_part2(line)
        result += x
        print(line, x, result)
    print(result)
