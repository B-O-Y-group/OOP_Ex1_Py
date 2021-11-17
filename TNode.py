from binarytree import Node

from BTraffic import *


class T_Node:

    def __init__(self, left, right, value):
        self.range = {"i": left, "j": right}
        self.value = value
        self.flag: bool = True

        self.split = {"x": left, "y": right}


    def allocate(self, x, y):
        self.flag = False
        self.set_split(x, y)

    def set_split(self, x, y):
        self.split["x", "y"] = x, y
