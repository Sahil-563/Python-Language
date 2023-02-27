class number():   #parent class or super class
    def __init__(self):
        self.num = 0
    def increase(self):
        self.num += 1
    def decrease(self):
        self.num -= 1

class new_num(number): #child class or sub class #it will inherit all the methods from number class or we can call parent clas
    def __init__(self):
        super().__init__()
    def sho_val(self):
        print(f"value: {self.num}")

num = new_num()
num.increase() #here we can access the methods of class number by the object of new_num class
num.decrease()
num.sho_val()