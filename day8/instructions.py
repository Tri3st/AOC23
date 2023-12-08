from day8.element import Element


class Instructions:
    def __init__(self, data):
        self.directions = data[0]
        self.elements = []
        self.step = 0
        self.init(data[2:])

    def init(self, data):
        for line in data:
            e = Element(line)
            self.elements.append(e)

    def traverse(self):
        current = self.elements[self.get_index_of_element("AAA")]
        while True:
            new_direction = self.directions[self.step % len(self.directions)]
            print(f"Step: {self.step}")
            print(f"Direction: {self.directions[self.step % len(self.directions)]}")
            print(f"Current: {current.value} .. next : {current.go(self.directions[self.step % len(self.directions)])}")
            print("\n")

            new_direction = self.directions[self.step % len(self.directions)]
            if current.value == "ZZZ":
                print("END")
                break
            else:
                index_of_next = self.get_index_of_element(current.go(new_direction))
                print(index_of_next)
                current = self.elements[index_of_next]
            self.step += 1

    def multi_traverse(self):
        current = []
        for element in self.elements:
            if element.is_start_element():
                current.append(element)
        while True:
            new_direction = self.directions[self.step % len(self.directions)]
            print(f"Step: {self.step}")
            print(f"Direction: {new_direction}")
            new_current = []
            for c in current:
                print(f"Current: {c.value} .. next : {c.go(new_direction)}")
                print("\n")
                new_current.append(self.elements[self.get_index_of_element(c.go(self.directions[self.step % len(self.directions)]))])
            current = new_current
            self.step += 1
            if len([y for y in current if y.is_end_element()]) == len(current):
                print("END")
                break
            if self.step == 10:
                break

    def get_index_of_element(self, value):
        for index, element in enumerate(self.elements):
            if element.value == value:
                return index
        return -1

    def __str__(self):
        result = f"Instructions: \n"
        for e in self.elements:
            result += f"{e}\n"
        return result

