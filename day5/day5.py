from day5.earth import Earth

f = open("day5/input_day5.txt", "r")
datalines = f.read().split("\n\n")
f.close()

datalines2 = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""".split("\n\n")


def part1():
    # Your code for part 1 goes here
    # First the small one :

    # seeds = [int(x) for x in datalines2[0].split(": ")[1].split(" ")]
    # earth = Earth(seeds)
    #
    # for row in datalines2[1:]:
    #     earth.add_operation(row)
    #
    # Then the big one .. :
    seeds = [int(x) for x in datalines[0].split(": ")[1].split(" ")]
    earth = Earth(seeds)

    # print(seeds)

    for row in datalines[1:]:
        earth.add_operation(row)
    #
    earth.test_seeds()
    print(earth.solutions)
    print("Lowest : ", earth.get_lowest_solution()[1])


def part2():
    # Your code for part 2 goes here
    seeds_temp = [int(x) for x in datalines[0].split(": ")[1].split(" ")]
    seeds = []
    for ind, seed_num in enumerate(seeds_temp):
        if ind % 2 == 0:
            for i in range(seed_num, seed_num + seeds_temp[ind + 1]):
                seeds.append(i)

    print(seeds)

    # earth = Earth(seeds)

    # for row in datalines[1:]:
    #     earth.add_operation(row)
    # #
    # earth.test_seeds()
    # print(earth.solutions)
    # print("Lowest : ", earth.get_lowest_solution()[1])
