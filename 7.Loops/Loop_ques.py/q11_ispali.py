    #without using [::-1] slicing

x = input("enter a string: ")
y=x.lower()
len1 = len(y)
for ele in range(0,int(len1/2)):
    if y[ele] != y[len(y)-ele-1]:
        print("This is not a pallidrome string")
        break
else:
    print("This is a pallidrome str")
