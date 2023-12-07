from day5.seed import Seed


class Earth:
    def __init__(self, seeds):
        self.TYPE = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]
        self.seeds = seeds
        self.solutions = []
        self.earth = []

    def get_seed(self, dest_type):
        for seed in self.earth:
            if seed.get_type() == dest_type:
                return seed
        return None

    def add_operation(self, data):
        rows = data.split("\n")
        header = rows[0]
        times = len(rows[1:])
        multi_row = [[int(x) for x in rows[1 + j].split(" ")] for j in range(times)]
        headers = header.split(" ")[0]
        ent = Seed()
        for row in multi_row:
            if headers == 'seed-to-soil':
                ent.add_mapping(row[0], row[1], row[2], self.TYPE[0], self.TYPE[1])
            elif headers == 'soil-to-fertilizer':
                ent.add_mapping(row[0], row[1], row[2], self.TYPE[1], self.TYPE[2])
            elif headers == 'fertilizer-to-water':
                ent.add_mapping(row[0], row[1], row[2], self.TYPE[2], self.TYPE[3])
            elif headers == 'water-to-light':
                ent.add_mapping(row[0], row[1], row[2], self.TYPE[3], self.TYPE[4])
            elif headers == 'light-to-temperature':
                ent.add_mapping(row[0], row[1], row[2], self.TYPE[4], self.TYPE[5])
            elif headers == 'temperature-to-humidity':
                ent.add_mapping(row[0], row[1], row[2], self.TYPE[5], self.TYPE[6])
            elif headers == 'humidity-to-location':
                ent.add_mapping(row[0], row[1], row[2], self.TYPE[6], self.TYPE[7])
        self.earth.append(ent)

    def test_seed(self, seed_nr):
        new_seed_nr = seed_nr
        print("Testing seed: ", new_seed_nr)
        seed = self.get_seed(self.TYPE[0])
        while True:
            new_seed_nr2 = seed.map(new_seed_nr)
            print(new_seed_nr, " -> ", seed.get_type(), " -> ", new_seed_nr2)
            new_destination = seed.get_destination()
            seed = self.get_seed(new_destination)
            new_seed_nr = new_seed_nr2
            if seed.get_type() is self.TYPE[6]:
                new_seed_nr = seed.map(new_seed_nr)
                break
        return new_seed_nr

    def test_seeds(self):
        for seed in self.seeds:
            self.solutions.append((seed, self.test_seed(seed)))

    def get_lowest_solution(self):
        if self.solutions:
            return min(self.solutions, key=lambda x: x[1])

    def __str__(self):
        result = "EARTH : \n"
        for i in self.earth:
            result += str(i) + "\n"
        return result
