# Passing parameter to class as a string and printing its result as integer or doing calculations as int()
class numeric_str():
    def __init__(self,Str):
        self.Str=Str
    def __int__(self):
        return int(self.Str)
num=numeric_str("100")
product = int(num.Str) * 2
print(product)



