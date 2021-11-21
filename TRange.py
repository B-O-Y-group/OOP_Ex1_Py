import Esort
from TNode import *
from BTraffic import *
from Esort import *
from CallList import CallList


class TRange:
    def __init__(self, b_traffic: BTraffic, e_sorted: ESort):
        self.e_sort = e_sorted
        self.BOOBO = b_traffic
        self.root = TNode(b_traffic.getMinFloor(), b_traffic.getMaxFloor(),
                          b_traffic.get_traffic(b_traffic.getMinFloor(), b_traffic.getMaxFloor()))
        self.pointer = 1
        self.max_list = []

    def addAfterSplit(self, t_node: TNode, traffic: BTraffic):
        parent_elev = t_node.elev_id
        parent_range_left = t_node.range["i"]
        parent_range_right = t_node.range["j"]
        # print("parent_range_right ", )
        x = str(t_node.split.get("x"))
        y = str(t_node.split.get("y"))
        new_t_node = TNode(x, y, traffic.get_traffic(int(x), int(y)))
        t_node.mid = new_t_node
        t_node.mid.set_elev(parent_elev)
        self.max_list.append(t_node.mid)
        if x != str(parent_range_left) and int(x) - int(parent_range_left) > 1:
            t_node.left = TNode(parent_range_left, int(x), traffic.get_traffic(parent_range_left, int(x)))
            t_node.left.set_elev(parent_elev)
            self.max_list.append(t_node.left)
        if y != str(parent_range_right) and int(parent_range_right) - int(y) > 1:
            t_node.right = TNode(int(y), parent_range_right, traffic.get_traffic(int(y), int(parent_range_right)))
            t_node.right.set_elev(parent_elev)
            self.max_list.append(t_node.right)

    def search_for_el(self, root: TNode, src, des, curr_call: CallForElevator):
        if root.left is None and root.mid is None and root.right is None:
            BTraffic.get_el_by_id(self.BOOBO, root.elev_id).call_queue.append(curr_call)
            return root

        if node_is_not_null(root.left):
            if int(root.left.range["i"]) <= int(src) and int(des) <= int(root.left.range["j"]):
                return self.search_for_el(root.left, src, des, curr_call)
        if node_is_not_null(root.mid):
            if int(root.mid.range["i"]) <= int(src) and int(des) <= int(root.mid.range["j"]):
                return self.search_for_el(root.mid, src, des, curr_call)
        if node_is_not_null(root.right):
            if int(root.right.range["i"]) <= int(src) and int(des) <= int(root.right.range["j"]):
                return self.search_for_el(root.right, src, des, curr_call)

        BTraffic.get_el_by_id(self.BOOBO, root.elev_id).call_queue.append(curr_call)

        return root


def node_is_not_null(root: TNode):
    if root is not None:
        return True
