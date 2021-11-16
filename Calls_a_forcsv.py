class Calls_a_forcsv:

    # הוא לא רלוונטי ולמעשה הוא לא נקרא ע״י המערכת בדיקה שלנו,
    # (שימו לב לסדר העמדות: עמודה 1: סתם מחרוזת, עמודה 2: זמן, עמודה 3: קומת מקור,
    # עמודה 4: קומת יעד, עמודה 5 סטטוס מעלית (לא במימוש - אפשר להתעלם)
    # , עמודה 6: שיבוץ למעלית (אינדקס), אחרי עמודה 6 המידע לא נקרא - אין לו חשיבות.)
    def __init__(self, str="Elevator call", time=0, src=0, dest=0, type=0, index=0) -> None:
        self.str = str
        self.time = time
        self.src = src
        self.dest = dest
        self.type = type
        self.index = index

    def __str__(self) -> str:
        return f"Str: {self.str} time : {self.time} src : {self.str} dest : {self.dest} type: {self.type} index: {self.index}"

    def __repr__(self) -> str:
        return f"Str: {self.str} time : {self.time} src : {self.str} dest : {self.dest} type: {self.type} index: {self.index}"
