import numpy as np
import json

from Building import Building
from CallList import CallList


class BTraffic(Building):
    def __init__(self, file: json, calls: CallList):
        super().__init__(file)
        self.traffic_list = {}
        self.src_dest_range = {}
        floor = self.getMinFloor()
        print(self.get_num_floor())
        self.listo = calls
        ''' Init the List of Traffic int the building (all floors get value - 0) '''
        for i in range(self.get_num_floor()):
            self.traffic_list[str(floor)] = 0
            self.src_dest_range[str(i)] = 0
            floor += 1
        print(self.traffic_list, "first")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ", self.src_dest_range)

        ''' { "3" : ++'''
        for i in range(len(calls.listcall)):
            # print("CURR CALL ---->", calls.listcall.__getitem__(i))
            self.traffic_list[str(calls.listcall.__getitem__(i).get_src())] += 2
            self.src_dest_range[
                str(abs(int(calls.listcall.__getitem__(i).get_src()) - int(calls.listcall.__getitem__(i).get_dest())))] += 1
            for j in range(int(calls.listcall.__getitem__(i).get_src()) + 1,
                           int(calls.listcall.__getitem__(i).get_dest())):
                self.traffic_list[str(j)] += 1
            self.traffic_list[str(calls.listcall.__getitem__(i).get_dest())] += 2
        print(self.traffic_list)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ", self.src_dest_range)

        self.sorted_range_list = {k: v for k, v in sorted(self.src_dest_range.items(), key=lambda item: item[1])}

        self.sorted_range_list = list(self.src_dest_range.keys())
        # self.sorted_range_list.sort(reverse=True)
        print(self.sorted_range_list)

    def get_traffic(self, left, right):
        t_sum = 0
        for i in range(int(left), int(right) + 1):
            t_sum += self.traffic_list.get(str(i))
        return t_sum

# if __name__ == '__main__':
#     d = BTraffic('B1.json', )
#     print(d.traffic_list)
