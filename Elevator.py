class Elevator:

    def __init__(self, _id, _speed, _minFloor, _maxFloor, _closeTime, _openTime, _startTime, _stopTime):
        self.id = id
        self.speed = _speed
        self.min_floor = _minFloor
        self.max_floor = _maxFloor
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

    def horse_power(self) -> float:
        openT = self.open_time()
        closeT = self.close_time()
        stopT = self.stop_time()
        startT = self.stop_time()
        speed = 1 / self.get_speed()

        return (openT + closeT + stopT + startT + 1 / speed)

    def __lt__(self, other):
        return Elevator.horse_power(self) > other

    def __str__(self) -> str:
        return f" {self.id},{self.speed}"

    def __repr__(self):
        return f" {self.id}, {self.speed}"
