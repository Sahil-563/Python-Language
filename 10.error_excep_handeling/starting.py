#errors and exception handeling in python:---
a = int(input("Enter you number: "))
b = int(input("Enter your number: "))
try:
    print("Resource opened")
    print(a//b)
except ZeroDivisionError:   
    print("0 can't be used in denominator")
except ValueError:
    print("sorry sonmething went wrong")
finally:
    print("Resource closed")
a = -20
b = 5
print(a//b)