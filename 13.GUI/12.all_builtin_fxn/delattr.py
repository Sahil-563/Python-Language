class Number():
    def __init__(self,name,value):
        self.name = name
        self.value= value
    def sho(self):
        print(self.name,self.value)
ob = Number("Sahil",12)
ob.sho()
delattr(ob,name)