# Description: Cube class
class Cube:
    def __init__(self, color: str, amount: int):
        self.color = color
        self.amount = amount

    def __str__(self):
        return f"{self.color} {self.amount}"
