#Method overriding:--
class Student():
    def name(self):
        print("sahil")
class teacher(Student):
    def name(self):
        print("vishal")
ob = teacher()
print(ob.name())

#variable overriding:--
class student():
    name = "sahil"
    roll_no = 2001010407
class show_details(student):
    name = "Vishal"      #here we overrided a variable "name"
ob = show_details()
print(ob.name())

