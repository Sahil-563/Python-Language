class op():
    def __init__(self,num):
        self.num = num
    def __add__(self,y):  #op.__add__(ob1,ob2)  here op.__add__(33,22)
        self.sum = self.num + y.num
        return self.sum


ob1 = op(33)
ob2 = op(22)
ob3 = ob1+ob2
print(ob3)