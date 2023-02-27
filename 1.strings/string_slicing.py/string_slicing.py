x="Sahil is good boy"
"""print(x[0:10])     #indexing
print(x[0:10])  #indexing a full line
print(x[0:5:2])   #step indexing
print(x[::])
print (x[0:-1]) #negative slicing
print(x[::-1])    #reversig a string
print(x[::-3])"""

    #string functons:----
print(x.endswith("sahil"))
print(len(x))
print(x.upper())
print(x.lower())
print(x.count("a"))
print(x.replace("is","are"))
print(x.capitalize())

#AVERAGE OF NUMBERS:-----
x,y,z=input("enter your numbers").split(",")
c=(int(x)+int(y)+int(z))/3
print(int(c))