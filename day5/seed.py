class Seed:
    def __init__(self):
        # { dest_type: None,
        #   mapping: { source: dest }
        # }
        self.type = None
        self.mapping = {
            "dest_type": None,
            "mapping": {}
        }

    def add_mapping(self, dest, source, rnge, src_type, dest_type):
        dest = [(dest + x) for x in range(rnge)]
        source = [(source + x) for x in range(rnge)]
        self.mapping['dest_type'] = dest_type
        for s, d in zip(source, dest):
            self.mapping['mapping'][s] = d
        self.type = src_type

    def get_type(self):
        return self.type

    def get_destination(self):
        return self.mapping['dest_type']

    def map(self, num):
        if num in self.mapping['mapping'].keys():
            return self.mapping['mapping'][num]
        else:
            return num

    def __str__(self):
        return f"SEED {self.type} {self.mapping}"
