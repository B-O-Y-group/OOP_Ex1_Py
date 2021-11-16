

class Elevator:


    def __init__(self, d) : #id, speed, min_floor, max_floor, close_time, open_time, start_time, stop_time):
        self.id = d['_id']
        self.speed = d['_speed']
        self.min_floor = d['_minFloor']
        self.max_floor = d['_maxFloor']
        self.close_time = d['_closeTime']
        self.open_time = d['_openTime']
        self.start_time = d['_startTime']
        self.stop_time = d['_stopTime']




    def get_speed(self):
        return self.speed

    def get_min_floor(self):
        return self.min_floor

    def get_max_floor(self):
        return self.max_floor

    def close_time(self):
        return self.close_time()
    def open_time(self):
        return self.open_time()

    def start_time(self):
        return self.open_time()

    def stop_time(self):
        self.stop_time()
        