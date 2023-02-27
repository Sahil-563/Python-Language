#enumerate built-in function is used to print the iterables of a list or any string with their indexes
x=[1,2,3,4,5,4]
for ind,ele in enumerate(x,start=0):   #enumerating a list
    print(ind,':',ele)
print("\n")
name = "Sahil"
for ind,ele in enumerate(name,start=100):  #enumerating a string
    print(ind,':',ele ," ", end="")
print("\n")
tpl=(1,2,3)
for ind,ele in enumerate(tpl):
    print(ind,':',ele)