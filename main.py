
import csv

from Calls_a_forcsv import Calls_a_forcsv

if __name__ == '__main__':
    row = []
    oly = []
    with open("Calls_a.csv") as file:
        csvreadr = csv.reader(file)
        header = next(csvreadr) ## next return the first line of  csvreader , header be the line of our data

        for row in csvreadr:
            o = Calls_a_forcsv( str= row[0], time=row[1], src=row[2], dest=row[3], type=row[4], index=row[5])
            oly.append(o)
            row.append(row) ## add what lest to row (list)


    print(header)
    print(row)
    print(oly)