class student():
    def sho(self,name=None):
        if name is not None:
            print("Hello "+name)
        else:
            print("Hello")
obj = student()
obj.sho()  #Here no value is given to name so only hello will be printed
obj.sho("Sahil")  #Here we passed an argument in sho so it will print hello+name
#Here we called sho method in many ways

