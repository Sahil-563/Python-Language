#vars :-- This is used to print the variables names anfd values corresponding to that variable
class person():
    name = "sahil"
    age = 22
    Roll_no = 2001014047
    def __init__(self):
        self.name = "Vishal"
        self.age = 19
        self.roll = 200101947
ob = person()
#print(vars(person))
print(vars(ob))