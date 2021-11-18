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

    def search_for_el(self, root: TNode, src, des):

        if root.left is None and root.mid is None and root.right is None:
            return root

        if root.range["i"] <= root.left.range["i"] and root.left.range["j"] <= root.range["j"] and is_in_range(root.left):
            return self.search_for_el(root.left, root.left.range["i"], root.left.range["j"])
        if root.range["i"] <= int(root.mid.range["i"]) and int(root.mid.range["j"]) <= root.range["j"] and is_in_range(root.mid):
            return self.search_for_el(root.mid, root.mid.range["i"], root.mid.range["j"])
        if int(root.range["i"]) <= int(root.right.range["i"]) and int(root.right.range["j"]) <= int(root.range["j"]) and is_in_range(root.right):
            return self.search_for_el(root.right, root.right.range["i"], root.right.range["j"])

        return root


def is_in_range(root: TNode):
    if root is None:
        return False
