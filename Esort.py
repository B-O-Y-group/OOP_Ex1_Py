import Building
from BTraffic import BTraffic
from Elevator import *
from CallForElevator import *
from Building import *
import numpy as np


class ESort:

    def __init__(self, b: BTraffic):
        self.sort_elev = b.get_el_list()
        self.sort_elev.sort()

    def __str__(self):
        return f" {self.sort_elev}"
