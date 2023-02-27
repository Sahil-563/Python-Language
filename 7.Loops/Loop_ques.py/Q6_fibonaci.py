 # Write a Program to Display Fibonacci Series upto certain number n (n is entered by user) 
 # Example: n=100 Output: Fibonacci Series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 
 
x=int(input("Enter a number upto which you want to calculate fibanaci series: "))
a=0
b=1
sum=0
while(sum<=x):
    print(sum)
    a=b
    b=sum
    sum=a+b



                                #or
x=int(input("Enter a fibonaci number upto which you want to calculate fibanaci series: "))
a=0
b=1
sum=0
for ele in range(0,x):
    if sum > x:
        break
    
    print(sum)
    a=b
    b=sum
    sum=a+b
    
    
    
    