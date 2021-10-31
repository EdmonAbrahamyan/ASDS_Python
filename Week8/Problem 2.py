class My_Time:
    def __init__(self, t: str):
        self.time = t

    def printTime(self):
        print(f"The current time is {self.time}")

class My_Date:
    def __init__(self, d: str):
        self.date = d

    def printDate(self):
        print(f"The current date is {self.date}")

class Date_Time(My_Time, My_Date):
    def __init__(self, t, d):
        My_Time.__init__(self, t)
        My_Date.__init__(self, d)

dt = Date_Time("12 PM", "13.03.2013")
dt.printDate()
dt.printTime()