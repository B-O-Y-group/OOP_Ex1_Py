import Building
from BTraffic import BTraffic
from Elevator import *
from CallForElevator import *
from Building import *
import numpy as np


class ESort:

    def __init__(self, b: BTraffic):

        self.sort_elev = b.get_el_list()
        print(self.sort_elev)
        self.sort_elev.sort()
        print("___________________________________________________>>>>>>>>>>>>>>>>", self.sort_elev)





# if __name__ == '__main__':
#     print("here!!!")
#     test = ESort(BTraffic('B5.json'))
#     print(test.sort_elev)
