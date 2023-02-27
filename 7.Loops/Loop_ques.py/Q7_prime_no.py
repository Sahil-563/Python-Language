# Question:---- Write a Program to Check Whether a Number is Prime or Not

x=int(input("enter a number: "))
for num in range(2,x):
    if x%num==0:
        print("This is not a prime number")
        break
else:
    print("This is prime number")

               #or
x=int(input("enter a number: "))
i=2
while(i<x):
    if x%i==0:
        print("This is not a prime number")
        break
    i+=1
else:
    print("This is prime number")
