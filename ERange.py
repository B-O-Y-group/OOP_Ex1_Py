from TRange import TRange
from BTraffic import *
from Esort import *


class ERange:
    def __init__(self, traffic_list: BTraffic, el_list: ESort):
        self.range_tree = TRange
        self.t_list = traffic_list
        self.elevator_list = el_list.sort_elev

