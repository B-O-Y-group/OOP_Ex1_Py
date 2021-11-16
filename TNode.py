from binarytree import Node


class T_Node:

    def __init__(self, left, right, traffic):
        in_range = {"i": left, "j": right}

        self.traffic = traffic

        flag: bool = True

        self.split = {"x": left, "y": right}


    def set_false(self, x, y):
        flag = False
        self.set_split(x, y)

    def set_split(self, x, y):
        self.split["x", "y"] = x, y
