import json
import csv

from BTraffic import BTraffic

class MainAlgo:
    def __init__(self, b_json: json, calls: csv):
        b_traffic = BTraffic(b_json)
        sorted_el_list = Esort(b_traffic)
