import json
import csv

from BTraffic import BTraffic
from ERange import *
from Esort import ESort
from CallList import CallList


class MainAlgo:
    def __init__(self, b_json: json, calls: csv):
        # for_test_building = 'B4.json'
        # for_test_calls = "Calls_a.csv"
        self.list_of_calls = CallList(calls)
        b_traffic = BTraffic(b_json, self.list_of_calls)
        print("!!!!!!!!!!!!!!!!!", b_traffic.traffic_list)
        sorted_el_list = ESort(b_traffic)
        e_range = ERange(b_traffic, sorted_el_list)

        print("SORTED ELEVATOR LIST ", sorted_el_list)

        print("Ultimate TEST ", e_range.range_tree.search_for_el(e_range.range_tree.root, 2, 3))
        for i in self.list_of_calls.listcall:
            i.set_index(e_range.range_tree.search_for_el(e_range.range_tree.root, i.src, i.dest).elev_id)
            # self.fixed_call_list.append(curr)

        print(self.list_of_calls.listcall)

    def calls_to_csv(self):
        file = 'output.csv'
        output_list = []
        for i in self.list_of_calls.listcall:
            output_list.append(i.__dict__.values())

        with open(file, 'w', newline="") as file:
            item = csv.writer(file)
            item.writerows(output_list)


if __name__ == '__main__':
    test = MainAlgo('B4.json', "Calls_a.csv")
    test.calls_to_csv()
