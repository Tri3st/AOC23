from MyMods.ReadDataFile import read_data
from day2.game import Game

datalines = read_data("day2/input_day2.txt")

datalines2 = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".split("\n")


def part1():
    # Your code for part 1 goes here
    comp = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    results = []
    final_results = []
    for line in datalines:
        g = Game(line)
        results.append(g)
    for result in results:
        print(result.game_nr, result.get_most_grabs())
        if result.compare_to(**comp):
            final_results.append(result.game_nr)
    print("Final results : ", final_results)
    total = sum([int(x) for x in final_results])
    print("Total : ", total)


def part2():
    # Your code for part 2 goes here
    comp = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    results = []
    final_results = []
    sums = []
    for line in datalines:
        g = Game(line)
        results.append(g)
    for result in results:
        print(result.game_nr, result.get_most_grabs())
        final_results.append(result.get_powers())
        sums += [result.get_powers()]
    print("Final results : ", final_results)
    print("Sums : ", sums)
    print("Sum of sums : ", sum(sums))

