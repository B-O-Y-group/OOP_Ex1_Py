from CallForElevator import callForElevator
from Elevator import Elevator

import csv
class callList:

    def __init__(self, file):
        row = []
        call=[]
        with open(file,'r+') as f:
            csvreader = csv.reader(f)

            for row in csvreader


