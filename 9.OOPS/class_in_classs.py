class student():
    def __init__(self):
        self.name = input("Enter your name: ")
        self.rollno = input("Enter your roll_no.")
    def show_val(self):
        print(f"Name: {self.name}\nRoll_no.: {self.rollno}")

    class Class():
        def __init__(self):
            self.std = input("Enter your class: ")
std1 = student()
std2 = student()
std1.show_val()
std2.show_val()
ob1=std1.Class()
ob2 = std2.Class()
print(f"{std1.name} is in class {ob1.std}")
print(f"{std2.name} is in class {ob2.std}")

