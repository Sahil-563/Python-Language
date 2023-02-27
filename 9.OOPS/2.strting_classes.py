class Employee:
    no_of_leaves=30
    salary=20000
    pass

Sahil=Employee()
Rohan=Employee()

Sahil.name="Sahil"
Sahil.role="web development"


Rohan.name="Roham"
Rohan.role="App development"
Rohan.salary=30000                      #here it creates an instance variable of rohan not changing the salary of employees
Employee.salary=40000                   #we can only change the salary of employees by calling the instance of classs emp means
                                         #you can acsess class variables with instance var but can only change with class var
print(Sahil.__dict__)
print(Rohan.__dict__)                   #dict attribute returns the dictionary of variable's key value pairs 
print(Sahil.salary)