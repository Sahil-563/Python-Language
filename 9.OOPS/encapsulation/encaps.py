#enapsulation done on a method update
class my_class():
    def __update(self):
        print("update")
    def update(self):
        print("updating again")
    def sho(self):
        self.__update()
class my_class2(my_class):
    pass
ob = my_class2()
ob.sho()

class class1():
    def __init__(self):
        self.__update()
    def __update(self):
        print("you are using a private method")
ob = class1()

#Encapsulation done on variables:
class private():
    __name = "sahil"    #this is a privte variable
    def show(self):     #this show method is public and can be accecible form anywhere and it contians the value of private variable __name
        print(self.__name)
class public(private):
    pass
ob = public()
ob.show()


