import json

from Building import Building
from CallList import CallList


class BTraffic(Building):
    def __init__(self, file: json, calls: CallList):
        super().__init__(file)
        self.traffic_list = {}
        self.src_dest_range = {}
        floor = self.getMinFloor()
        self.listo = calls
        ''' Init the List of Traffic int the building (all floors get value - 0) '''
        for i in range(self.get_num_floor()):
            self.traffic_list[str(floor)] = 0
            self.src_dest_range[str(i)] = 0
            floor += 1

        ''' { "3" : ++'''
        for i in range(len(calls.listcall)):
            self.traffic_list[str(calls.listcall.__getitem__(i).get_src())] += 2
            self.src_dest_range[
                str(abs(
                    int(calls.listcall.__getitem__(i).get_src()) - int(calls.listcall.__getitem__(i).get_dest())))] += 1
            for j in range(int(calls.listcall.__getitem__(i).get_src()) + 1,
                           int(calls.listcall.__getitem__(i).get_dest())):
                self.traffic_list[str(j)] += 1
            self.traffic_list[str(calls.listcall.__getitem__(i).get_dest())] += 2

        self.sorted_range_list = {k: v for k, v in
                                  sorted(self.src_dest_range.items(), reverse=True, key=lambda item: item[1])}

        self.val_range_list = list(self.sorted_range_list.values())
        self.final_range_list = []
        for i in range(len(self.get_el_list())):
            self.final_range_list.append(self.get_key(self.val_range_list.__getitem__(i)))

    def get_traffic(self, left, right):
        t_sum = 0
        for i in range(int(left), int(right) + 1):
            t_sum += self.traffic_list.get(str(i))
        return t_sum

    def get_key(self, val):
        for key, value in self.sorted_range_list.items():
            if val == value:
                return key

        return "key doesn't exist"
