import Esort
from TNode import *
from BTraffic import *
from Esort import *


class TRange:
    def __init__(self, b_traffic: BTraffic, e_sorted: ESort):
        self.e_sort = e_sorted
        self.root = TNode(b_traffic.getMinFloor(), b_traffic.getMaxFloor(),
                          b_traffic.get_traffic(b_traffic.getMinFloor(), b_traffic.getMaxFloor()))
        self.pointer = 1
        self.max_list = []

    def addAfterSplit(self, t_node: TNode, traffic: BTraffic):
        print("in addAfterSplit func ", t_node.split.get("x"), t_node.split.get("y"))
        parent_range_left = t_node.range["i"]
        parent_range_right = t_node.range["j"]
        # print("parent_range_right ", )
        x = str(t_node.split.get("x"))
        y = str(t_node.split.get("y"))
        new_t_node = TNode(x, y, traffic.get_traffic(int(x), int(y)))
        t_node.mid = new_t_node
        self.max_list.append(t_node.mid)
        if x != str(parent_range_left) and int(x) - parent_range_left > 1:
            t_node.left = TNode(parent_range_left, int(x), traffic.get_traffic(parent_range_left, int(x)))
            self.max_list.append(t_node.left)
        if y != str(parent_range_right) and parent_range_right - int(y) > 1:
            t_node.right = TNode(int(y), parent_range_right, traffic.get_traffic(int(y), parent_range_right))
            self.max_list.append(t_node.right)
