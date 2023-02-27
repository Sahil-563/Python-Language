class grandparent():
    house = 1
class parent(grandparent):
    car = 1
class child(parent):
    bike = 1
ob = child()
print(ob.house)

class coder:
    def code(self):
        print("codin")
class pythoneer(coder):
    def python(self):
        print("Coding in python")
class django(pythoneer):
    def we_dev(self):
        print("Building a website")

obj1 = django()
obj1.code()
obj1.python()
obj1.we_dev()

