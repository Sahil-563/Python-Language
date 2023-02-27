                  #dictionary are identified by "{}"
                  #key and value pairs

dict={}  #blank dictionary
print(type(dict))
d1={"priyanka":"veg",
    "sahil":"junkfood",
    "arpit":{"b":"chowmin","l":"rasmalai"}}
    
print(d1["priyanka"])
d1.update({"sunny":"tati"})
print(d1)
print(d1["arpit"]["b"])
print(d1.keys())
print(d1.items())  
d2=d1.copy() #copies the dictionary from d1 to d2 change made in d2 don't affect d1 nd if it was like d2=d1 then it affects
del d2["arpit"]    #delete a key from tha dictionary
print(d2)
print(d1)
print(d1.get("sahil"))
