class CallForElevator:
    def __init__(self, str="Elevator call", time=0, src=0, dest=0, type=0, index=0) -> None:
        self.str = str
        self.time = time
        self.src = src
        self.dest = dest
        self.type = type
        self.index = index

    def set_index(self, data):
        self.index = data

    def get_src(self):
        return self.src

    def get_dest(self):
        return self.dest

    def get_time(self):
        return self.time


    def __lt__(self, other):
        return self.time < other

    def __str__(self) -> str:
        return f"Str: {self.str} time : {self.time} src : {self.src} dest : {self.dest} type: {self.type} index: {self.index}"

    def __repr__(self) -> str:
        return f"Str: {self.str} time : {self.time} src : {self.src} dest : {self.dest} type: {self.type} index: {self.index}"
