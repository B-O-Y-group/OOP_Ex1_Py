import Building
from BTraffic import BTraffic
from Elevator import *
from CallForElevator import *
from Building import *
import numpy as np


class ESort:

    def __init__(self, b: Building):

        self.sort_elev = b.get_el_list().sort()


if __name__ == '__main__':
    print("here!!!")
    test = ESort(Building('B2.json'))
    print(test.sort_elev)
