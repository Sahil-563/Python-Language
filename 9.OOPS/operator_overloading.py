#operator overloadding :--- using a single operator with multiple functions like "+" is used in python to add two integer
#as well as used to concatinate two strings with each other

class algebra():
    def __init__(self,r=0.0,i=0.0):
        self.real = r
        self.imag = i
    def __add__(self,y):  #it will work as:-- algebra.__add__(num1,num2) means self will be num1 and y will be num2
        self.real = self.real + y.real
        self.imag = self.imag + y.imag
        return self
    def show_val(self):
        print(self.real,self.imag)

num1 = algebra(4.4,6.6)
num2 = algebra(4.4,6.6)
num3=num1 + num2  #now we want to add the real part of num1 to real part of num1 and imag part of num2 to imag part of num1
                  #for that we uses a builtin class method that is __add__ 
num3.show_val()

       

