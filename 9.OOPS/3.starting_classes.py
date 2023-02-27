#constructor :-- To give args to the employee class that thing is known as constructor
class Employee:
    def __init__(self,aname,arole):  #here __init__ is constructor
        self.name=aname
        self.role=arole
    def printdetails(self): #here self is that instance or object of class on which that fxn example printdetails is being implemented
       return f"Name is {self.name}\nRole is {self.role}"
Sahil=Employee("Sahil","web development")
Rohan=Employee("Rohan","App development")


#Sahil.name="Sahil"
#Sahil.role="web development"


#Rohan.name="Rohan"
#Rohan.role="App development"
#print(Rohan.printdetails())   #we donot give argument inside a function in classes this is the convention of oops
print(Sahil.printdetails())
##print(Rohan.role)