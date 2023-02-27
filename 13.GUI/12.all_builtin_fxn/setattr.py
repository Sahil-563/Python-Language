#setattr:-- This is used to set a attribute in a class and in a function
class student():
    def __init__(self,name):
        self.name = name
    def sho_val(self):
        print(self.name)
        print(locals())
ob = student("Sahil")
ob.sho_val()
setattr(ob,'name','Vishal')  #It can be used to change the corresponding attribute value
print(ob.name)
setattr(ob,'age',22)  #It is used to add a new attribute
print(ob.age)
