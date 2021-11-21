import json
import csv

from BTraffic import BTraffic
from ERange import *
from Esort import ESort
from CallList import CallList


class MainAlgo:
    def __init__(self, b_json: json, calls: csv):
        self.list_of_calls = CallList(calls)
        b_traffic = BTraffic(b_json, self.list_of_calls)
        sorted_el_list = ESort(b_traffic)
        self.test = b_traffic
        e_range = ERange(b_traffic, sorted_el_list)
        for i in self.list_of_calls.listcall:
            i.set_index(e_range.range_tree.search_for_el(e_range.range_tree.root, i.src, i.dest, i).elev_id)

    def calls_to_csv(self):
        file = '../output.csv'
        output_list = []
        for i in self.list_of_calls.listcall:
            output_list.append(i.__dict__.values())

        with open(file, 'w', newline="") as file:
            item = csv.writer(file)
            item.writerows(output_list)


if __name__ == '__main__':
    test = MainAlgo('json file/B5.json', "csv file/Calls_d.csv")
    test.calls_to_csv()
