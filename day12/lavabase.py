from day12.lavacode import LavaCode


class LavaBase:
    def __init__(self, data):
        self.lavas = []
        for line in data:
            l = LavaCode(line)
            self.lavas.append(l)

    def __str__(self):
        return "\n".join([str(l) for l in self.lavas])