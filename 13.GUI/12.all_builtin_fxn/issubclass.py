class sub(str):
    pass
ob = sub()
print(issubclass(sub,str))   #sub is the subclass of str
  
      #for another class
class add(int):
    def __init__(self,num):
        if num%2 == 0:
            self.val = num
        else:
            self.val = num-num%2
print(issubclass(add,int))  #This will check that is evennumber is the subclass of int
ob = add(4)
print(ob.val+3)   #By this function we can add any value without getting any typeerror
