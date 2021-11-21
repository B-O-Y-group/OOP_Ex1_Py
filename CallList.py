from CallForElevator import CallForElevator
import csv


class CallList:
    def __init__(self, csvfile):
        self.call = []
        try:
            with open(csvfile, 'r') as file:
                csvread = csv.reader(file)
                for row in csvread:
                    c = CallForElevator(str=row[0], time=row[1], src=row[2], dest=row[3], type=row[4], index=row[5])
                    self.call.append(c)

                self.listcall = self.call



        except IOError as exp:
            print('my exp - ', exp)
