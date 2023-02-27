class error(ValueError):   #user defined error
    "can't divide a number by zero"
try:
    x= int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    if y != 0:
        pass
    else:
        raise error
except error:
    print(error.__doc__)
except Exception:
    print("Sorry something went wrong")
else:
    print(x/y)    #else part is executed when there is no error in the program
finally:
    print("Execution Done!")  #finally block always get printed by the compiler either 
                              #the program encounters an error or not 

                              #or
class Cubeerror(Exception):
    "sorry cube can't be zero"
class cube():
    def __init__(self,num):
        #num = int(num)
        self.num = int(num)
        if self.num != 0:
            pass
        else:
           raise Cubeerror
try:
    obj = cube(input("Enter a number: "))
    obj2 = cube(input("Enter another number: "))
except Cubeerror:
    print(Cubeerror.__doc__)
except Exception:
    print("Sorry something went wrong!")
else:
    print(obj.num**obj2.num)
finally:
    print("Execution Completed!")

