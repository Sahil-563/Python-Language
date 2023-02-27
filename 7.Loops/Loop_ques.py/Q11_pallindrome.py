#Question:---Write a Program to Check Whether a Number N entered by user is Palindrome or No
num=int(input("Enter a number: "))
temp=num
rev_no=0
while num > 0:
    lst_digit=num%10   #if we divide any number with 10 
                       #we always get the last digit of the dividend as remainder 
                        
    rev_no=rev_no*10+lst_digit
    num//=10
if rev_no==temp:
    print(f"{rev_no} is a palindrome no.")
else:
    print(f"{rev_no} is not a palindrome no.")