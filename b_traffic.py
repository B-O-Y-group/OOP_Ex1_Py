# from CallList import *
import numpy as np
from Building import *


class BTraffic:
    def __init__(self, call_list, b_json):
        b = Building('B1.json')
        self.traffic_list = {}
        floor = b.getMinFloor()
        print(7)
        for i in range(b.getMaxFloor() - b.getMinFloor() + 1):
            self.traffic_list[str(floor)] = 0
            floor += 1
        print(self.traffic_list)


def main():
    a = BTraffic(6, 7)


if __name__ == '__main__':
    main()
