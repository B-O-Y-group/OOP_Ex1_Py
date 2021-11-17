import json
import csv

from BTraffic import BTraffic
from Esort import ESort
from CallList import CallList


class MainAlgo:
    def __init__(self, b_json: json, calls: csv):
        for_test_building = 'B1.json'
        for_test_calls = "Calls_a.csv"
        list_of_calls = CallList(for_test_calls)
        b_traffic = BTraffic('B1.json', list_of_calls)
        sorted_el_list = ESort(b_traffic)


if __name__ == '__main__':
    MainAlgo('B1.json', "Calls_b.csv")
