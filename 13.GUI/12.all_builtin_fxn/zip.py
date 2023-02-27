#zip():--zip function is used to zip two elements of a list in a tuple
names = ["Sahil","Vishal",'Aman']
age = [19,20,20]
z=zip(names,age)
print(z)
for names,ages in zip(names,age):  #('Sahil',19)
    print(names,"age is",ages)