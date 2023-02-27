#callable function is used to return true or false 
#True if the function is callable
#False if the function is not callable

def Print():
    print("Sahil")
print(callable((Print)))     #In this case the Print function is callable

class now():
    def __init__(self):
        self.name = "sahil"
    def _private(self):
        self.name = "sahil"
        print(self.name)
ob = now()
print(callable(ob._private()))  #In this case thr _private method is not callable