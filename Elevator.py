class Elevator:

    def __init__(self, _id, _speed, _minFloor, _maxFloor, _closeTime, _openTime, _startTime, _stopTime):
        self.id = _id
        self.speed = _speed
        self.min_floor = _minFloor
        self.max_floor = _maxFloor
        self.close_time = _closeTime
        self.open_time = _openTime
        self.start_time = _startTime
        self.stop_time = _stopTime
        self.horse_power = 1 / (self.close_time + self.open_time + self.start_time + self.stop_time) + self.speed
        self.call_queue = []

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

    def __lt__(self, other):
        return self.horse_power > other.horse_power

    def __str__(self) -> str:
        return f" {self.id},{self.speed}"

    def __repr__(self):
        return f" id{self.id},speed {self.speed},min floor {self.min_floor},max floor {self.max_floor}"


if __name__ == "__main__":
    e1 = Elevator(1, 3, 10, 10, 10, 10, 10, 10)
    e2 = Elevator(2, 2, 10, 10, 10, 10, 10, 10)
    e3 = Elevator(3, 5, 10, 10, 10, 10, 10, 10)
    e5 = Elevator(4, 4, 10, 10, 10, 10, 10, 10)

    list = [e1, e2, e3, e5]
    print(list)
    list.sort()
    print(list)
