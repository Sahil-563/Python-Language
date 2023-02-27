#Question:---Find the LCm of two numbers entered by the user

#In coding the LCM=Least common multiple of two numbers
#eg:--Multiple of 2:--2,4,6,8,10,12,14...
#     Multiple of 3:--3,6,9,12,15,18,21...
#     here least common multiple is 6
#    so lcm=6

num1=int(input("Enter a number: "))           
num2=int(input("Enter a number: "))
if num1>num2:
    higher=num1
else:
    higher=num2
value=higher
while True:
    if higher%num1==0 and higher%num2==0:
        print(f"The L.C.M of {num1},{num2} = {higher}")
        break
    higher+=value   #higher=higher+value:--6=3+3