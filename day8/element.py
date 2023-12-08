import re


class Element:
    def __init__(self, data):
        pattern = r"^(\w{3}) = \((\w{3}), (\w{3})\)$"
        data2 = re.findall(pattern, data)[0]
        print(data2)
        self.value = data2[0]
        self.left = data2[1]
        self.right = data2[2]

    def go(self, direction):
        if direction == "L":
            return self.left
        elif direction == "R":
            return self.right
        else:
            return "ERROR"

    def is_end_element(self):
        return self.value[2] == "Z"

    def is_start_element(self):
        return self.value[2] == "A"

    def __str__(self):
        return f"{self.value} = ({self.left} {self.right})"
