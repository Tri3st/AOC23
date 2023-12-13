from MyMods.ReadDataFile import read_data
from day12.lavabase import LavaBase

datalines = read_data("day12/input_day12.txt")

datalines2 = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""".split("\n")

    
def part1():
    # Your code for part 1 goes here
    lb = LavaBase(datalines2)
    print(lb)

        
def part2():
    # Your code for part 2 goes here
    pass
