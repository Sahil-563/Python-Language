#Question:---Write a Program to Generate Multiplication Table of a number (entered by the user) using a for loop
x=int(input("Enter a number: "))
for a in range(1,11):
    c=x*a
    print("{} * {} = {}".format(x,a,c))

                    #using while loop:-----

x=int(input("Enter a number: "))
i=1
while i<=10:
    result=x*i
    print("{} * {} = {}".format(x,i,result))
    i+=1



