""" Question:---- Write a program to know a number is even or odd"""


x=int(input("enter a number\n"))
if x%12==0:
    print("{} is an even number".format(x))
else:
    print("{} is a odd number".format(x))
