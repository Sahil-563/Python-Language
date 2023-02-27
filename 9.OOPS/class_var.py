class coder:
    def __init__(self):
        self.name="sahil"  #    These are local variables and you can access them outside the cla
      
    lang="python"
    _age=19        #private variable adding underscore beside a var. means you are not allowed to access the var outside the class
    __clg="J.N.G.E.C"   #adding two underscores means you are strictly prihibited to use the var outside the classs
    
        
x=coder()
x.__init__()     #you should not call double score variables outside the class
print(x.name)
