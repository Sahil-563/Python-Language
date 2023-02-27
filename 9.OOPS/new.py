class students():
    def __init__(self,name,std,number):
        self.name = name
        self.std = std
        self.num = number
    def details(self,language=None):
        if language == None:
            pass
        print(f"Name of the student is: {self.name}\nClass of the student is: {self.std}\nLanguage = {language}\nMobile no: {self.num}")

student1 = students("Sahil","12TH",9805420563)
student2 = students("Vishal","10th",8894388210)
#student1.details("Hindi")
student2.details("English")
del(student1.name)



