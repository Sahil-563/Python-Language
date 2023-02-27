                                     #OPERATIONS IN TUPLES

tpl=tuple("sahil")
#tuple methods are:---
print(tpl.index('a'),tpl.count('a'))
print(tuple(sorted(tpl)))  #after sorting tuple always return a list so if you want to tuple convert it into a tuple again
print(len(tpl))
tpl2=(1,3,4,5,5,6)
print(min(tpl2),max(tpl2))
tpl3=(1,2,4,5,6)
print(tpl3)
tpl4=("sahil","vishal",1,3)  
print(len(tpl4))   #len fxn counts the no. of elements inside a tuple
tpl5=(12,17,11,21)
print(sum(tpl5))
print((tpl))