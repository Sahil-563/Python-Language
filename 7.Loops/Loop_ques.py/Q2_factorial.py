"""question 2:----
             Calculate the factorial of a number and get the number as input from user"""


x=int(input("Enter the number whose factorial you want to calculate: "))
fact=1
for c in range(1,x+1):
    fact=c*fact
print(fact)


x=int(input("Enter the number whose factorial you want to calculate: "))
fact=1
i=x
while i>=0:
    fact = fact * i
    i-=1
print(fact)

