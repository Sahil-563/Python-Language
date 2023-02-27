#hasattr always print the result in boolean form in the form of True or False
#It is used to know that a prticular attribute is present in a particular class or in an object or a object have that particular
#attribute/instance or not
class student():
    Class = "Student"
    def __init__(self,name,age):
        self.name = name
        self.age = age
ob = student("sahil",60)
print(hasattr(ob,'name'))  #since ob has instance or attribute name so it will return true
print(hasattr(student,'age'))  #now it will return false since student class has no control on age instance or object
print(hasattr(student,"Class"))  #now it will return true since it has Class as an object