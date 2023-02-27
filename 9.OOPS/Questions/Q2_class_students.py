class students():
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
    def info(self):
        print(f"Name: {self.name}\nRoll no.: {self.roll_no}")
    def set_age(self,age):
        self.age = age
        return self.age
    def set_marks(self,marks):
        self.marks = marks
        return self.marks

Student1 = students("Sahil",20010104047)
Student2 = students("Akshita",20010104007)
Student1.info()
print(f"Marks: {Student1.set_marks(44)}")
print(f"age: {Student1.set_age(19)}")