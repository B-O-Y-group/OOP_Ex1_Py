import callList
from Elevator import Elevator

import json


class Building:

    def __init__(self, min_floor, max_floor):

        self.count = 0  # how many elevator
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.elevator = []

    def load(self, file):
        try:
            with open('file', 'r+'):
                data = json.loads(file)

                self.min_floor = data["_minFloor"]
                self.max_floor = data["_maxFloor"]

                for i in data['_elevators']:
                    elev = Elevator("_id", "_speed", "_minFloor", "_maxFloor", "_closeTime", "_openTime", "_startTime",
                                    "_stopTime")

                self.elevator.append(elev)
            self.ElevatorList = self.elevator


        except IOError as exp:
            print(exp)

    def __str__(self) -> str:
        return f"{self.elevator}\n cont:{self.count}"

if __name__ == '__main__':
    file = r"Users/97252/Downloads/Ex1_input (1)/Ex1_input/Ex1_Buildings/B1.json"

    b1 = Building(file)

    print(b1.max_Floor)
