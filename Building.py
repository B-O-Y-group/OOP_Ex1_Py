import CallList
from Elevator import Elevator

import json


class Building:
    def __init__(self, file):

        try:
            f = open(file)

            with open(file, 'r+'):
                data = json.load(f)
                self.min_floor = data["_minFloor"]
                self.max_floor = data["_maxFloor"]
                self.elevator = []

                for i in data['_elevators']:
                    elev = Elevator(**i)

                    self.elevator.append(elev)
            self.ElevatorList = self.elevator

        except IOError as exp:
            print('my exp - ', exp)

    def get_el_list(self):
        return self.ElevatorList

    def getMaxFloor(self):
        return self.max_floor

    def getMinFloor(self):
        return self.min_floor

    def get_num_floor(self):
        return (self.max_floor - self.min_floor) + 1
