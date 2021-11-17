import numpy as np
from Building import *
from CallForElevator import *
from CallList import *

class BTraffic(Building, CallList, callForElevator):
    def __init__(self, file):
        super().__init__(file)
        b = Building(file)
        self.traffic_list = {}
        floor = b.getMinFloor()
        print(b.get_num_floor())

        for i in range(b.get_num_floor()):
            self.traffic_list[str(floor)] = 0
            floor += 1
        print(self.traffic_list)

    def lulaa_mekunenet(self,):


# def main():
    # a = BTraffic(7,'B1.json')


if __name__ == '__main__':
    d= BTraffic('B1.json', 'Calls_a.csv')
    print(d)
