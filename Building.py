import callList
from Elevator import Elevator

import json


class Building:

    def __init__(self, file):
        self.elevator = []
        self.count = 0  # how many elevator
      #  try:
        with open('files', 'r+') as f:

                data = json.loads(file)  # read the fill and make it array

                self.min_floor = data["_minFloor"]
                self.max_floor = data["_maxFloor"]

                for i in data['_elevators']:

                  #  elev = Elevator("_id", "_speed", "_minFloor", "_maxFloor", "_closeTime", "_openTime",
                              #     "_startTime",
                               #     "_stopTime")
                    self.elevator.append(Elevator(i))

        f.close()
        #except IOError as exp:
         #   print(exp)






    # def __str__(self) -> str:
    #     return f"{self.elevator}\n cont:{self.count}"


file1 = r"Users\97252\Downloads\Ex1_input (1)\Ex1_input\Ex1_BuildingsB1.json"

b1 = Building(file1)

print(b1.max_Floor)