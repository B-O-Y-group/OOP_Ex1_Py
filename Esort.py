import Building
from BTraffic import BTraffic
from Elevator import *
from CallForElevator import *
from Building import *
import numpy as np


class ESort:

    def __init__(self):

        btra = Building('B1.json')
        self.elev_list = btra.get_el_list()

        # self.elev_list = np.sort

    def __str__(self):
        return f" {self.elev_list(iter())}"


if __name__ == '__main__':
    print("here!!!")
    test = ESort()
    print(test.elev_list)
