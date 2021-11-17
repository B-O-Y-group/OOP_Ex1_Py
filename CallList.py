from CallForElevator import cc
import csv


class callList:

    def __init__(self, csvfile):
        self.call = []
        try:
            with open(csvfile, 'r') as file:
                csvread = csv.reader(file)
                for row in csvread:
                    c = cc(str=row[0], time=row[1], src=row[2], dest=row[3], type=row[4], index=row[5])
                    self.call.append(c)

                self.listcall = self.call
                print(self.call)


        except IOError as exp:
            print('my exp - ', exp)


if __name__ == '__main__':
    callList("Calls_b.csv")

    # row = []
    #
    # with open("Calls_a.csv") as file:
    #         csr = csv.reader(file)
    #
    #
    #         for r in csr:
    #             row.append(r)
    #
    # print(row)
