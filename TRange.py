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

    def add(self, data: TNode, dir):
        if self.pointer < len(self.e_sort.sort_elev):
            curr = data.dir

