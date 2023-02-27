def isprime(x):
    flag =1
    for ele in range(2,x+1):
        if x%ele==0:
            flag=0
            return flag
    return flag

def nextprime(y):
    y=y+1
    y=int(y)
    for ele in range(2,y+1):
        if y%ele==0:
            break
    else:
        return y

    

num=input("Enter a number")
num=int(num)
print(type(num))
i=2
print(type(i))
while i<=num-i:
    if (isprime(num-i)):
        print(f"{i} + {num-i} = {num}")
    i=nextprime(i)
    


