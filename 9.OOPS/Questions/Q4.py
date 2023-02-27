class Time():
    def __init__(self):
        self.hr = int(input("Enter the hours: "))
        self.min = int(input("Enter the minutes: "))
    def __add__(self,y):
        self.hr=self.hr+y.hr
        self.min = self.min +y.min
        if self.min > 60:
            while self.min>60:
                self.hr += 1
                self.min -= 60
        return self
    def displaytime(self):
        print(f"{self.hr} hours {self.min} minutes")
    def display_minute(self):
        self.temp2 = 0
        self.hr=round(self.hr*60)
        self.temp2 = self.hr+self.min
        print(f"{self.temp2} minute")

time1 = Time()
time2 = Time()
time3 = (time1+time2)
time3.displaytime()