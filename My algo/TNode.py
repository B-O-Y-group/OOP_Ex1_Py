class TNode:

    def __init__(self, i, j, value):
        self.range = {"i": i, "j": j}
        self.get_range_space = int(j) - int(i)
        self.value = value
        self.flag: bool = True
        self.split = {"x": i, "y": j}

        self.elev_id = None

        self.right = self.left = self.mid = None

    def set_elev(self, e_id):
        self.elev_id = e_id

    def allocate_to_node(self, x, y):
        self.flag = False
        self.value -= 2 * self.value
        self.set_split(x, y)

    def set_split(self, x, y):
        self.split["x"] = x
        self.split["y"] = y

    def __lt__(self, other):
        return self.value > other.value

    def __str__(self):
        return f" {self.range},{self.flag},{self.value},{self.split}, {self.elev_id}"

    def __repr__(self):
        return f" {self.range},{self.flag},{self.value},{self.split}, {self.elev_id}"
