class Instruction:
    def __init__(self, instr):
        self.part = None
        self.operator = None
        self.second_part = None
        self.result = None
        self.REJECTED = None
        self.ACCEPTED = None
        if ":" in instr:
            tmp = instr.split(":")
            tmp2 = None
            if ">" in tmp[0]:
                self.operator = ">"
                tmp2 = tmp[0].split(">")
            elif "<" in tmp[0]:
                self.operator = "<"
                tmp2 = tmp[0].split("<")
            self.part = tmp2[0]
            self.second_part = int(tmp2[1])
            self.result = tmp[1]
        else:
            self.result = instr
        self.executed = False
        if self.result == "A":
            self.ACCEPTED = True
        elif self.result == "R":
            self.REJECTED = True

    def get_result(self):
        return self.result

    def is_end(self):
        return self.ACCEPTED or self.REJECTED

    def __str__(self):
        res = ""
        if self.operator:
            res = f"{self.part} {self.operator} {self.second_part} : {self.result}"
        else:
            res = f"{self.result}"
        return res
