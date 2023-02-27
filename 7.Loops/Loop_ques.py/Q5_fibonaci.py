#Question:-----Write a Program to Display Fibonacci Series upto nth term (n is entered by user)


x=int(input("Enter the number upto which you want to calculate fibonaci series of fisrt n natural numbers: "))
a=0
b=1
sum=0
for num in range(1,x+1):
    print(sum)
    a=b
    b=sum
    sum=a+b
    
                              
                              #using while loop:---
x=int(input("Enter the number upto which you want to calculate fibonaci series of fisrt n natural numbers: "))
a=0
b=1
sum=0
i=1
while i<=x:
   
    print(i,sum)
    a=b
    b=sum
    sum=a+b
    
    i+=1
