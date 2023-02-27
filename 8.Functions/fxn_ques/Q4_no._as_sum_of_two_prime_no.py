#Write a Program to check if an integer (entered by the user) can be expressed as the sum of two prime numbers,
# if yes then print all possible combinations with the use of functions. Example Enter a positive integer: 
# 34 OUTPUT: 34 = 3 + 31 34 = 5 + 29 34 = 11 + 23 34 = 17 + 17

def isprime(num):
    lst1=[]
    for ele in range(2,num+1):
        for i in range(2,ele):
            if ele%i==0:
                break
        else:
            lst1.append(ele)
    return lst1

num=int(input("Enter a number: "))
lst1=isprime(num)
x=0
lst2=[]
for ele in lst1:
    x=num-ele
    if x>1:
        for c in range(2,x):
            if x%c==0:
                break
        else:
            lst2.append(x)
lst3=lst2

for i in lst1:
    for j in lst3:
        if i + j == num:
            print(f"{i} + {j} = {num}")
    
        

            









        






