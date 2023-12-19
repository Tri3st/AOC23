from day19.rule import Rule
from day19.workflow import Workflow


class System:
    def __init__(self, data):
        data_temp = data.split("\n\n")
        self.rules = []
        self.workflows = []
        self.accepted = []
        self.rejected = []
        for rule in data_temp[0].split("\n"):
            self.rules.append(Rule(rule))
        for workflow in data_temp[1].split("\n"):
            self.workflows.append(Workflow(workflow))

    def walk(self, workflow_id):
        start = [rule for rule in self.rules if rule.name == "in"][0]
        workflow = self.workflows[workflow_id]
        while True:
            temp = start.get_result(workflow)
            print("temp : ", temp)
            if temp == "A":
                self.accepted.append(workflow_id)
                break
            elif temp == "R":
                self.rejected.append(workflow_id)
                break
            else:
                start = [rule for rule in self.rules if rule.name == temp][0]

    def __str__(self):
        rules = ""
        for rule in self.rules:
            rules += f"{rule}\n"
        workflows = ""
        for workflow in self.workflows:
            workflows += f"{workflow}\n"
        return f"Rules:\n{rules}\nWorkflows:\n{workflows}"
