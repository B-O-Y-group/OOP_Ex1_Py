import CallList
from Elevator import Elevator
import json


class Building:


    def __init__(self, file):
        self.min_floor = 0
        self.max_floor = 10
        self.elevator = []


    def loadjson(self, file):
        try:
            with open('file', 'w') as f:
                data = json.loads(file)

                elev = Elevator("id", "speed","min_floor", "max_floor", "close_time", "open_time", "start_time", "stop_time")
                self.elevator.append(elev)

        except IOError as exp:
            print(exp)



