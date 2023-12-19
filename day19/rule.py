import re

from day19.instruction import Instruction
from day19.workflow import Workflow


class Rule:
    def __init__(self, rule):
        """
        instructions: {
            part: "x, m, a, s"
            operator: ">" or "<",
            second_part: "x, m, a, s"
            result: "any other rule name"
            } or
            {
             result: "accept" or "reject" or "rule name"
            }
        :param rule:
        """
        pattern = r"^(\w+){(.*)}$"
        matches = re.findall(pattern, rule)
        self.name = matches[0][0]
        self.instructions = []
        for instr in matches[0][1].split(","):
            print("instr : ", instr)
            self.instructions.append(Instruction(instr))

    def get_result(self, workflow: Workflow):
        result = None
        for inst in self.instructions:
            if inst.is_end():
                return inst.get_result()
            elif inst.operator:
                if inst.operator == ">":
                    if workflow.get_value(inst.part) > inst.second_part:
                        return inst.get_result()
                elif inst.operator == "<":
                    if workflow.get_value(inst.part) < inst.second_part:
                        return inst.get_result()
            else:
                return inst.get_result()

    def __str__(self):
        instructions = ""
        for instr in self.instructions:
            instructions += f"{instr}, "
        return f"{self.name}: {instructions}"[:-2]


