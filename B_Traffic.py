# from CallList import *
# from Numpy import *

class B_Traffic(Building):
    def __init__(self, call_list, b_json):
        super().__init__(b_json)
        self.traffic_list = {}
        for i in range(Building.max_floor - Building.min_floor):
            floor = Building.min_floor
            str_floor = "" + floor
            traffic_list[str_floor] = 0
            floor += 1


def main():
    a = B_Traffic(6, 7)
    print(a.traffic_list)


if __name__ == '__main__':
    main()
