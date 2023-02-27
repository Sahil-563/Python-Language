#hash():--only work wit immutable objects such as tuples
var = "sahil"
print(hash(var))
tpl = (1,2,3)  #These are immutable
print(hash(tpl))
lst = [1,3,4]  #It will give error since it is unhashable
print(hash(lst))
