import json
import csv

from BTraffic import BTraffic
from ERange import ERange
from Esort import ESort
from CallList import CallList


class MainAlgo:
    def __init__(self, b_json: json, calls: csv):
        for_test_building = 'B1.json'
        for_test_calls = "Calls_a.csv"
        list_of_calls = CallList(for_test_calls)
        b_traffic = BTraffic('B2.json', list_of_calls)
        sorted_el_list = ESort(b_traffic)
        e_range = ERange(b_traffic, sorted_el_list)


if __name__ == '__main__':
    MainAlgo('B1.json', "Calls_b.csv")
