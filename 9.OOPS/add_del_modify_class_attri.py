class coder():
    def __init__(self,name,language):
        self.Name=name
        self.lang=language
    def info(self):
        return self.Name,self.lang,self.best
    def ispython(self):
        if "Python" in self.lang:
            print(True)
        else:
            print(False)

cd=coder("Sahil",["Python","Java"])
print(cd.Name)
cd.best="python"
print(cd.info())
print(cd.best)
print(cd.info())

