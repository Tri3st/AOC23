import re


class Workflow:
    def __init__(self, workflow):
        """{x=1679,m=44,a=2067,s=496}"""
        pattern = r"([xmas])=(\d+)"
        matches = re.findall(pattern, workflow, re.MULTILINE)
        self.workflow = {
            'a': -1,
            'm': -1,
            's': -1,
            'x': -1
        }
        for match in matches:
            self.workflow[match[0]] = int(match[1])

    def get_value(self, part: str) -> int:
        return self.workflow.get(part)

    def __str__(self):
        return f"Workflow: x: {self.workflow['x']} m: {self.workflow['m']} a: {self.workflow['a']} s: {self.workflow['s']}"

