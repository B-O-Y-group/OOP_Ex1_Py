class TNode:

    def __init__(self, i, j, value):
        self.range = {"i": i, "j": j}
        self.value = value
        self.flag: bool = True
        self.split = {"x": i, "y": j}

        self.elev_id = None

        self.right = self.left = self.mid = None

    def set_elev(self, e_id):
        self.elev_id = e_id

    def set_false(self, x, y):
        self.flag = False
        self.set_split(x, y)

    def set_split(self, x, y):
        self.split["x", "y"] = x, y
