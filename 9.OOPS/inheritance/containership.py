class coder():
    names = ["sahil", "vishal" , "Ishan"]
    Languages = ["Python" , "C++" , "Java"]
    def __init__(self):
        self.name = input("Name: ")
        self.lang = input("Languages: ")
    def show_val(self):
        print(f"Name: {self.name}")
        print(f"Languages: {self.lang}")

class pythoneer():
    def __init__(self):
        self.profile = coder()
    def profile(self):
        self.profile.show_val()

sahil = pythoneer()
sahil.profile.show_val()