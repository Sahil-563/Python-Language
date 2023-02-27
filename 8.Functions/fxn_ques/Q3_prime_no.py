 #Question:--Write a Program to Display Prime Numbers Between Two Intervals (entered by the user) Using Functions:--
def isprime(num1,num2):
    for ele in range(num1,num2+1):
        if ele>1:
            for i in range(2,ele):
                if ele%i==0:
                    break
            else:
                print(ele)
x=int(input("Enter your 1st no: "))
y=int(input("ENter your 2nd no: "))
isprime(x,y)

