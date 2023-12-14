from day13.mirror import Mirror


class Mirrors:
    def __init__(self, mirrors):
        self.mirrors = []
        for mirror in mirrors:
            self.add_line(mirror)

    def add_line(self, data):
        self.mirrors.append(Mirror(data.split("\n")))

    def get_mirror(self, mirror_id):
        return self.mirrors[mirror_id]

    def __str__(self):
        return "\n".join([str(mirror) for mirror in self.mirrors])