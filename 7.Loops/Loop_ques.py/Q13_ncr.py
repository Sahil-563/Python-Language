def fac(value):
    fact = 1
    for ele in range(1,value+1):
        fact = fact * ele
    return fact


n = int(input("Enter your n: "))
r = int(input("Enter your r: "))
print(f"The answer is: {fac(n)/(fac(r)*fac(n-r))}")