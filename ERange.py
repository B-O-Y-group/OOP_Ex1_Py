from TNode import TNode
from TRange import TRange
from BTraffic import *
from Esort import *


class ERange:
    def __init__(self, traffic_list: BTraffic, el_list: ESort):
        self.t_list = traffic_list
        self.elevator_list = el_list.sort_elev
        self.range_tree = TRange(self.t_list, self.elevator_list)
        self.pointer = 0
        self.range_tree.root.set_elev(el_list.sort_elev.__getitem__(self.pointer).id)
        next_n = self.split(self.range_tree.root.range, 90)

        self.range_tree.root.set_split(next_n["i"], next_n["j"])

        print(self.range_tree.root.split)
        self.pointer += 1
        # print(len(el_list.sort_elev))
        # print(self.t_list.get_traffic(self.t_list.getMinFloor(), self.t_list.getMaxFloor()))
        # print(self.t_list.get_num_floor() / len(el_list.sort_elev))
        # print((self.t_list.get_traffic(self.t_list.getMinFloor(),
        #                                self.t_list.getMaxFloor()) // self.t_list.get_num_floor() * len(
        #     el_list.sort_elev)))

    def split(self, n_range: TNode, target):
        i = int(n_range["i"])
        val = self.t_list.get_traffic(i, i + 1) / 2
        ranges = {"left": i, "right": i + 1}

        while i < n_range["j"] - 1:
            j = i + 1
            while j < n_range["j"]:
                if self.t_list.get_traffic(i, j) / (j - i) > val and self.t_list.get_traffic(i, j) <= target:
                    print("we got true")
                    print(self.t_list.get_traffic(i, j))
                    val = self.t_list.get_traffic(i, j)
                    ranges["left"] = i
                    ranges["right"] = j
                j += 1
            i += 1

        return {"i": ranges["left"], "j": ranges["right"], "val": val}
    # while j <= right:
    #     while self.t_list.get_traffic(i, j) < target:
    #         j += 1
    #     if self.t_list.get_traffic(i, j) > val and j - i < num_index:
    #         val = self.t_list.get_traffic(i, j)
    #     i_pos = i
    #     while i < j:
    #         while self.t_list.get_traffic(i, j) < target:
    #             i -= 1
    #         if self.t_list.get_traffic(i, j) > val and j - i < num_index:
    #             val = self.t_list.get_traffic(i, j)
