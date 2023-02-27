#Quetion:--- Write a Program to Check whether a year entered by user is Leap Year or not

x=int(input("Enter a year"))
if x % 400 ==0:
    print("It is a leap year")
elif x%4==0 and x%100 != 0:
    print("It is a leap year")
else:
    print("It is not a leap year")
