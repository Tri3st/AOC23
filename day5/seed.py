class Seed:
    def __init__(self):
        # { dest_type: None,
        #   mapping: { source: dest }
        # }
        self.type = None
        self.mapping = {
            "dest_type": None,
            "mappings": []
        }

    def add_mapping(self, dest, source, rnge, src_type, dest_type):
        self.mapping['dest_type'] = dest_type
        self.type = src_type
        self.mapping['mappings'].append({
            "source": source,
            "dest": dest,
            "range": rnge
        })

    def get_type(self):
        return self.type

    def get_destination(self):
        return self.mapping['dest_type']

    def map(self, num):
        print(self.mapping['mappings'])
        curr_mapping = None
        for mapping in self.mapping['mappings']:
            if mapping['source'] <= num < mapping['source'] + mapping['range']:
                curr_mapping = mapping
                break
        if curr_mapping:
            diff = curr_mapping['dest'] - curr_mapping['source']
            return num + diff
        return num

    def __str__(self):
        return f"SEED {self.type} {self.mapping}"
