from binarytree import *
import numpy as np
from BTraffic import *


class TNode:

    def __init__(self, left, right, value):
        self.range = {"i": left, "j": right}
        self.value = value
        self.flag: bool = True

        self.split = {"x": left, "y": right}

    def set_split(self, i, j, target):
        self.target = target
        i = 
        while
        # sum_val = 0
        # count = 1
        # for a in range(i, j + 1):
        #     sum_val = sum_val + a
        #     count += 1
        #     if a > target:
        #         sum_val - a,
        #         break
        # return sum_val, count-1



    def allocate(self, x, y):
        self.flag = False
        self.set_split(x, y)

    def set_split(self, x, y):
        self.split["x", "y"] = x, y
