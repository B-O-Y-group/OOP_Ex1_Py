import json
import csv

from BTraffic import BTraffic
from ERange import *
from Esort import ESort
from CallList import CallList


class MainAlgo:
    def __init__(self, b_json: json, calls: csv):
        for_test_building = 'B1.json'
        for_test_calls = "Calls_a.csv"
        self.list_of_calls = CallList(calls)
        b_traffic = BTraffic(b_json, self.list_of_calls)
        sorted_el_list = ESort(b_traffic)
        self.test = b_traffic
        e_range = ERange(b_traffic, sorted_el_list)
        print("NUM OF CALLS ", len(self.list_of_calls.listcall))
        print("SORTED ELEVATOR LIST ", sorted_el_list)

        print("Ultimate TEST ", e_range.range_tree.search_for_el(e_range.range_tree.root, 2, 3))
        for i in self.list_of_calls.listcall:
            i.set_index(e_range.range_tree.search_for_el(e_range.range_tree.root, i.src, i.dest).elev_id)

        print(self.list_of_calls.listcall)
        print(len(self.test.get_el_by_id(0).call_queue))
        print(len(self.test.get_el_by_id(1).call_queue))
        print(len(self.test.get_el_by_id(2).call_queue))
        print(len(self.test.get_el_by_id(3).call_queue))
        print(len(self.test.get_el_by_id(4).call_queue))
        print("traffic ", self.test.get_traffic(self.test.getMinFloor(), self.test.getMaxFloor()))

    def calls_to_csv(self):
        file = 'output.csv'
        output_list = []
        for i in self.list_of_calls.listcall:
            output_list.append(i.__dict__.values())

        with open(file, 'w', newline="") as file:
            item = csv.writer(file)
            item.writerows(output_list)


if __name__ == '__main__':
    test = MainAlgo('B4.json', "Calls_c.csv")
    test.calls_to_csv()
