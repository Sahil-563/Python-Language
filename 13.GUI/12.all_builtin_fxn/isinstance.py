#isinstance() function is used to print that a particular object or a variable in the instance of a particular class or not

num = "Sahil"
#num = 90
#num = 90.0
if isinstance(num,str):
    print("This is a stirng")
elif isinstance(num,int):
    print("This is an integer")
else:
    print("This is a float value")

class student():
    nmae = "Sahil"
ob = student()
print(isinstance(ob,student))
