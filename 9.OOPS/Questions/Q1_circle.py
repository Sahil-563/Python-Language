# Question:-- create a circle class and initilixe it with radius. Make two methods getArea and getCircumference inside this class

class circle():
    def __init__(self,r):
        self.radius = r
    def getArea(self):
        return (3.14*(self.radius**2))
    def getCircumference(self):
        return (2*3.14*self.radius)

radius = circle(2)
print(radius.getArea())