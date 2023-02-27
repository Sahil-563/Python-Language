#overriding done on method:
class Student():
    def name(self):
        print("sahil")
class teacher(Student):
    def name(self):
        print("vishal")
ob = teacher()
ob.name()

#overriding done variable:
class arpit():
    name = "Lodu"
class adarsh(arpit):
    name = "Lodu2"
ob = adarsh()
print(ob.name)