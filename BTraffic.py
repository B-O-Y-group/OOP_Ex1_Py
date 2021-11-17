import numpy as np
import json

from Building import Building


class BTraffic(Building):
    def __init__(self, file: json):
        super().__init__(file)
        self.traffic_list = {}
        floor = self.getMinFloor()
        print(self.get_num_floor())

        for i in range(self.get_num_floor()):
            self.traffic_list[str(floor)] = 0
            floor += 1
        print(self.traffic_list)
    #
    # def lulaa_mekunenet(self,):
    #     for i in range()


# def main():
# a = BTraffic(7,'B1.json')


if __name__ == '__main__':
    d = BTraffic('B1.json')
    print(d.traffic_list)
