import callList
from Elevator import Elevator

import json


class Building:

    def __init__(self, file):

        self.count = 0  # how many elevator
        try:
            with open('file', 'r+'):
                data = json.loads(file)

                self.min_floor = data["_minFloor"]
                self.max_floor = data["_maxFloor"]
                self.elevator = []


                for i in data['_elevators']:
                 #  elev = Elevator("_id", "_speed", "_minFloor", "_maxFloor", "_closeTime", "_openTime",
                  #     "_startTime",
                           #     "_stopTime")
                        print(i)
                     #   self.elevator.append(Elevator(i))
              #  self.ElevatorList = self.elevator


        except IOError as exp:
             print(exp)


    def __str__(self) -> str:
         return f"{self.elevator}\n cont:{self.count}"

# if __name__ == '__main__':
#     file = r"Users/97252/Downloads/Ex1_input (1)/Ex1_input/Ex1_Buildings/B1.json"
#
#     b1 = Building(file)
#
#     print(b1.max_Floor)
