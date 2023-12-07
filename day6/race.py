class Race:
    def __init__(self, data):
        self.time = int(data[0])
        self.distance = int(data[1])
        self.wins = []

    def calc_race_times(self):
        for i in range(14, self.time + 1):
            if i <= self.time:
                speed = i
                distance = (self.time - i) * (speed)
                print(f"time : {i} distance {distance}")
                if distance > self.distance:
                    self.wins.append(i)

    def get_nr_of_wins(self):
        return len(self.wins)

    def __str__(self):
        return f"time : {self.time}, distance : {self.distance}\n"
