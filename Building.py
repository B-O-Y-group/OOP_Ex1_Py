
from Elevator import Elevator
import json
class Building:





def __init__(self):
    self.min_floor = 0
    self.max_floor = 10


def loadjson(self, file):
    try:
         with open('file', 'w') as f:
             data = json.loads(file)

         with open('Building.json.json', 'w') as f:
             json.dump(data, f, indent=2)
             

    except IOError as exp:
        print(exp)