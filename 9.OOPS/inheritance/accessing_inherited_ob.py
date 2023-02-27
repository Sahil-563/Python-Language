class number():
    new_number = 12 #PUBLIC VARIABLE
    _num = 32
    __num =12 #you cannot access this class variable outside this class even if this variable is inherited by another class
    def __init__(self):
        self.num = 0
    def increase(self):
        self.num += 1
    def decrease(self):
        self.num -= 1
class new_num(number):
    def __init__(self):
        super().__init__()
    def sho_val(self):
        print(self.num)
num = new_num()
num.increase()
print(num._num)
num.sho_val()