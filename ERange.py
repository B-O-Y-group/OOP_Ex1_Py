from TRange import TRange
from BTraffic import *
from Esort import *


class ERange:
    def __init__(self, traffic_list: BTraffic, el_list: ESort):
        self.t_list = traffic_list
        self.elevator_list = el_list.sort_elev
        self.range_tree = TRange(self.t_list, self.elevator_list)
        self.pointer = 0
        self.range_tree.root.set_elev(el_list.sort_elev.__getitem__(self.pointer))

    def split(self, left, right, target):
        i = int(left)
        val = self.t_list.get_traffic(i, i + 1) / 2
        ranges = {"left": i, "right": i + 1}

        while i < right - 1:
            j = i + 1
            while j < right:
                if self.t_list.get_traffic(i, j) / (j - i) > val and self.t_list.get_traffic(i, j) <= target:
                    val = self.t_list.get_traffic(i, j)
                    ranges["left", "right"] = i, j
                j += 1
            i += 1

        return {"i": ranges["left"], "j": ranges["left"], "val": val}
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
