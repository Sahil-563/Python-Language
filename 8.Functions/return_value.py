#Returning the value to a function 
#Function to calculate factiorial:----
def fact(num):
    result=1
    for ele in range(1,num+1):
        result=ele*result
    return result               #here we return the value of resukt to function fact

y=int(input("Enter a number: "))
result=fact(y)
print(result)

#Function of addition:--
def add(*num):
    sum=0
    for ele in num:
        sum=sum+ele
    return sum
result=add(12,34,5,6,7,8,8,9)
print(F"The sum is: {result}")

def char(x):
    x=x+"2"
    x=x*2
    return x
print(char("lets_code"))