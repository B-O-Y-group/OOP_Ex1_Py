from CallForElevator import callForElevator

import csv


class callList:

    def __init__(self, file):
        a = 1
        self.call = []
        try:
            with open(file, 'r') as file:
                csvread = csv.reader(file)
                for row in csvread:
                    c = callForElevator(str=row[0], time=row[1], src=row[2], dest=row[3], type=row[4], index=row[5])
                    self.call.append(c)
                self.listcall = self.call


        except IOError as exp:
            print('my exp - ', exp)


if __name__ == '__main__':
    print(callList('Calls_a.csv'))
