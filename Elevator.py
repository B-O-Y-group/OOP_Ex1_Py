

class Elevator:


    def __init__(self, _id, _speed, _minFloor, _maxFloor, _closeTime, _openTime, _startTime, _stopTime):
        self.id = id
        self.speed = _speed
        self.min_floor =_minFloor
        self.max_floor =_maxFloor
        self.close_time = _closeTime
        self.open_time = _openTime
        self.start_time = _startTime
        self.stop_time = _stopTime




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
