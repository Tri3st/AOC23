class Boxes:
    def __init__(self):
        self.boxes = {
            k: [] for k in range(256)
        }

    def get_labels_of_box(self, box_nr):
        return [x.get_label() for x in self.boxes[box_nr]]

    def add(self, word):
        box_nr = word.get_small_hash()
        labels = self.get_labels_of_box(box_nr)
        if word.get_sign() == "=":
            # do operator =
            if word.get_label() not in labels:
                self.boxes[box_nr].append(word)
            else:
                label = word.get_label()
                position = [index for index, w in enumerate(self.boxes[box_nr]) if w.get_label() == label][0]
                self.boxes[box_nr][position] = word
        else:
            # do operator -
            if word.get_label() in labels:
                this_word = [w for w in self.boxes[box_nr] if w.get_label() == word.get_label()][0]
                self.boxes[box_nr].remove(this_word)

    def calc_focusing_power(self):
        res = 0
        for box_nr, box in enumerate(self.boxes):
            for index, word in enumerate(self.boxes[box]):
                res += word.get_strength() * (index + 1) * (box_nr + 1)
        return res

    def __str__(self):
        res = ""
        for box in self.boxes:
            boxes = [f"{x.get_label()} {x.get_strength()}" for x in self.boxes[box]]
            res += f"{box}: {boxes}\n"
        return res