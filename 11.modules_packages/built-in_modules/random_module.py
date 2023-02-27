from random import *
print(round(random(),2))  #The random method prints the floating point numbers betweeen the range 0.0 to 1.0
print(randint(1,5))       #The randint function is used to print the integers from the given range of a to b
print(round(uniform(1.5,5)))  #The uniform method is used to print floating point numbers from the given range of a to b
print(randrange(0,10,2)) #The randrange function prints the number between the given range but can also take a third parameter which is used to give steps

def die(num):
    seed = num     #seed is used to get the use of multiple algorithms which are predefined in random meodule with different numbers
    return randint(1,6)
print(die(7)) 

x = [1,2,3,4]
shuffle(x)    #shuffle function shuffles the elements of the list
print(x)
print(choice(x))  #choice function is used to print the iterables or elements of the list in random
print(sample(x,3))  #Sample method is used to print the specified sample of elements of a list

x = list("Sahil")
print(choice(x))
print(sample(x,3))
