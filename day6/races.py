import re

from day6.race import Race


class Races:
    def __init__(self, data, part_two=False):
        pattern = r'(\d+)'
        line = data.split('\n')
        times = re.findall(pattern, line[0])
        distances = re.findall(pattern, line[1])
        if part_two:
            time = ""
            for t in times:
                time += str(t)
            times = [int(time)]
            distance = ""
            for d in distances:
                distance += str(d)
            distances = [int(distance)]
        self.races = [Race(x) for x in zip(times, distances)]
        self.wins = []

    def race(self):
        for race in self.races:
            race.calc_race_times()
            self.wins.append(race.get_nr_of_wins())

    def get_solution(self):
        sol = 1
        for win in self.wins:
            sol *= win
        return sol

    def __str__(self):
        result = ""
        for race in self.races:
            result += f"{race}"
        return result
