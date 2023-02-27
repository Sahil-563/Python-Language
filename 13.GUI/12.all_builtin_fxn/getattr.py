#getattr() is used to get the value of a  attribute from a class or a attribute
#attributes are the objects or instances of a function
class person():
    name = "Aman"
    def __init__(self,name,age):  #here name , age are attributes of ob object 
        self.name = name
        self.age = age
ob = person("sahil",12)  #here 
print(getattr(ob,"name"))   #this will print the value of name attribute 
print(ob.name)   #this will also print the value of name attribute
print(getattr(ob,"age"))  #this will print the value of age attribute

  #class person() has no access on name and age attribute since these are attributes or insatnces of object 
  # so you can only get the value of attribues of person class as
print(getattr(person,"name"))