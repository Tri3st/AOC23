import re
from day2.grab import Grab


class Game:
    def __init__(self, gameline):
        self.grabs = []
        self.maximums = {
            "blue": 0,
            "red": 0,
            "green": 0
        }
        pattern = r"^Game (\d+):.*$"
        regex = re.findall(pattern, gameline)
        self.game_nr = regex[0]
        lines = gameline.split(";")
        for line in lines:
            gr = Grab(line)
            self.maximums["blue"] += gr.get_amount("blue")
            self.maximums["red"] += gr.get_amount("red")
            self.maximums["green"] += gr.get_amount("green")
            self.grabs.append(gr)

    def get_most_grabs(self):
        result = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for grab in self.grabs:
            result["red"] = grab.get_amount("red") if grab.get_amount("red") > result["red"] else result["red"]
            result["green"] = grab.get_amount("green") if grab.get_amount("green") > result["green"] \
                else result["green"]
            result["blue"] = grab.get_amount("blue") if grab.get_amount("blue") > result["blue"] else result["blue"]
        self.maximums = result
        return result

    def compare_to(self, **kwargs):
        blue = kwargs["blue"]
        red = kwargs["red"]
        green = kwargs["green"]
        if self.get_most_grabs()["blue"] > blue:
            return False
        if self.get_most_grabs()["red"] > red:
            return False
        if self.get_most_grabs()["green"] > green:
            return False
        return True

    def get_powers(self) -> int:
        res = 1
        for maximum in self.maximums.values():
            res *= maximum
        return res

    def __str__(self):
        return f"Game {self.game_nr}: {self.grabs}"
