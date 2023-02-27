from abc import ABC, abstractmethod
class parent():
    @abstractmethod
    def fun1(self):
        pass
class child(parent):
    def fun1(self):
        print("This is child class")
ob = child()
ob.fun1()