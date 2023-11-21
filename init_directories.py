import os
import re

day_nr = None


def get_python_file(num):
    """
        creates the contents of the python file for each day

    :param num: the day of the challenge
    :return: formatted text for the python file
    """
    return f"""from MyMods.ReadDataFile import read_data
        
datalines = read_data("day{num}/input_day{num}.txt")

    
def part1():
    # Your code for part 1 goes here
    pass
    
        
def part2():
    # Your code for part 2 goes here
    pass
"""


matrix_file = f"""\"\"\" Matrix Class = for use with matrixes or grids.
use dimj -> dimensions rows
    dimi -> dimensions columns \"\"\"


class Matrix:
    \"\"\"
       Matrix class. makes a matrix with dimi colums and dimj rows
    \"\"\"

    def __init__(self, dimj, dimi):
        self.dimj = dimj
        self.dimi = dimi
        self.grid = [[0 for i in range(dimi)] for j in range(dimj)]
        self.lowpoints = []
        self.risklevel = 0

    def __str__(self):
        \"\"\"
           Returns a string representation of the matrix
        \"\"\"
        t = ""
        for j in range(self.dimj):
            for i in range(self.dimi):
                t += str(self.grid[j][i])
            t += \"\\n\"
        return t
        
"""

read_data_file = f"""\"\"\"Automated datafile reading\"\"\"
import os


def read_data(filename="", lines=0) -> list:
    \"\"\"
        Read all the data from a given text file
        use the input or give a filename in the string.
        for all lines leave ommit lines (default = 0)
        Parameters:
            filename (str): the filename 'day1/day1.txt'
            lines (int): number of lines to take (default = 0 = ALL)
        Returns:
            data (list): a list with the data lines.
    \"\"\"
    if not filename:
        filename = input("enter filename (day1/day1.txt) : ")
    first_x = lines
    data = []

    try:
        f = open(filename, "r")
        if first_x != 0:
            for i in range(int(first_x)):
                data.append(f.readline().strip())
        else:
            data = f.readlines()
            data = [d.strip() for d in data]
        f.close()
    except Exception as e:
        print("Oops. there was an error : %s" % e.__str__())

    return data
"""

for day_nr in range(1, 26):
    dir_name = f"day{day_nr}"
    parent_dir = "C:/Users/MartinvanDiest/AOC23/"
    path = os.path.join(parent_dir, dir_name)
    os.mkdir(path)


os.mkdir("C:/Users/MartinvanDiest/AOC23/MyMods")
mods_dir = "C:/Users/MartinvanDiest/AOC23/MyMods/"
file_path1 = os.path.join(mods_dir, "Matrix.py")
f = open(file_path1, "x")
f.write(matrix_file)
f.close()
file_path2 = os.path.join(mods_dir, "ReadDataFile.py")
f = open(file_path2, "x")
f.write(read_data_file)
f.close()

all_dirs = os.listdir("C:/Users/MartinvanDiest/AOC23")
my_dirs = [d for d in all_dirs if os.path.isdir(d) and not d.startswith(".")]

for my_dir in my_dirs:
    if my_dir.startswith("day"):
        daynr = int(my_dir.split("day")[1])
        file_name = f"day{daynr}.py"
        text_file_name = f"input_day{daynr}.txt"
        path = os.path.join(f"C:/Users/MartinvanDiest/AOC23/day{daynr}/", file_name)
        path2 = os.path.join(f"C:/Users/MartinvanDiest/AOC23/day{daynr}/", text_file_name)
        f = open(path2, "x")
        f.close()
        f = open(path, "x")
        f.write(get_python_file(daynr))
