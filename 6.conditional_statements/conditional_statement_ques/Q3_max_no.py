"""Question:-----
            Write a program to find the largest among three no. entered by a user"""

            
x=int(input("Enter 1st numbers: "))
y=int(input("Enter 2nd numbers: "))
z=int(input("Enter 3rd numbers: "))

if x>y and x>z:
     print(x)
elif y>x and y>z:
    print(y)
else:
    print(z)
     #or
#print(max(x,y,z))
