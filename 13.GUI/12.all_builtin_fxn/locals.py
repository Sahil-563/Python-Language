#All the values which are outside a class or a function are global variables
#All the values inside a class or function are local variables
Num = 0
def add(num):
    added_num = Num  #now this Num is global var so it can be used inside a function
                         #And this added_num is local variable which can't be used outside this function
    print(locals())      #This function will give the value of local variables
add(8)
