class coder():
    def __init__(self):
        self.name = input("Name: ")
class pythoneer():
    def __init__(self):
        self.works = input("works: ")
class web_dev(coder,pythoneer):
    def __init__(self):
        coder.__init__(self)
        pythoneer.__init__(self)
    def start_new(self):
        print("new.html")
web = web_dev()
web.start_new()

class student():
    def __init__(self):
        self.name = input("enter your name: ")
class roll_no():
    def __init__(self):
        self.roll_no = int(input("Enter your roll_no: "))
class details(student,roll_no):
    def __init__(self):
        student.__init__(self)
        roll_no.__init__(self)
    def sho_details(self):
        print(self.name)
        print(self.roll_no)
obj = details()
obj.sho_details()