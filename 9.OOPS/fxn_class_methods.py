class coder:
    def __init__(self,name):
        self.name=name
       
    def get_lang(self,*lst):   #this is a classs method
        self.lst=lst
        print(self.lst)

def ispython(lst):    #This is function outside the class
    if "python clsass " in lst:
        print(True)
    else:
        print(False)

cd = coder("Sahil")
cd.get_lang("Python","C++")
ispython(cd.name)





