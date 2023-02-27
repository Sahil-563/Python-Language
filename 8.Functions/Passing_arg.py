def greet(name):   #Here name is an argument which is inside in a function greet "It is a local variable"
                   #It can't be acceced outside the function bcs it is local variable
    print(f"Have a nice day! {name}")
    print(type(name))

greet(27)     #Here the argument is passed in a function named greet

                        #creating a program of addition using function:----
def sum(a,b):                 #here a and b are positional arguments
    print(a+b)                
sum(12,3)                      # a and b are positional args beacause they give their positions to the numbers 12 and 3

                           #Creating a program of substraction using a function :---
def substraction(a,b):
    result=a-b                
    print(result)
substraction(12,2)           #Here the position of args a nd b matters because 2 is subtreacted from 12


                            #There are two type of arguments :--
                            #1. positional args
                            #2. keyword agrs
                            #keyword args use arguments that are inside a function as keywords
#example:--
def result(name,marks):
    print(f"Name: {name}\nMarks: {marks}")
result(89,"sahil")                #here we doing this program using positioning name first then marks
                                  #but if we pass marks first in result function and name later then it will print
                                  #output:-- Name: 89 and Marks: Sahil

#Now to overcome this problem we can use keyword arguments as:
def result(name,marks):
    print(f"Name: {name}\nMarks: {marks}")
result(marks=89,name="sahil")      #here marks and name are used as keyword args
                                   


