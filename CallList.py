from CallForElevator import callForElevator
from Elevator import Elevator


class CallList:

    def __init__(self, num_of_call):
        self.num_of_call = num_of_call # = callForElevator
        call_list = []
        for i in range(0, num_of_call):
            call_list.append([])

    def get_num_of_calls(self):
        return self.num_of_call


    # def horse_power(self, src, dest, elev: Elevator):
    # stop_time = elev.stop_time
    # start_time = elev.start_time
    # open_time = elev.open_time
    # close_time = elev.close_time
    # speed = elev.speed
    # dis = abs(src - dest)
    # time = stop_time + start_time + open_time + close_time
    # how_many_stop = callList[0]  ##idk
    #
    # return (time + dis / speed) * how_many_stop

