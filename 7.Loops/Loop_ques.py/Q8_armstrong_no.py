#question:---Write a Program to check whether a number entered by the user is an Armstrong number or not
x=int(input("enter the number: "))

sum=0
temp=x
while x!=0:
    
    digit=x%10
    power=pow(digit , 3)
    sum=sum+power
    x//=10
if temp==sum:
    print("This is an armstrong number")
else:
    print("This is not an armstrong number")



