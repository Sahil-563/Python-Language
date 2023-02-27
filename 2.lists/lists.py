                        #lists are mutible(can be changed)
                        
x=["sahil","vishal","ishan",32,4]

print(x.index("sahil"))
print(x[2])
numbers=[2,32,4,67,8]
numbers[1]=44   #lists are mutible 
print(numbers) 
numbers.sort() 
#variable.sort()  #inbuit functions in python which sort the list and changes the original list
#variable.reverse() #inbuilt function in python which reverse the list and changes the original list
print(numbers)

#slicing in lists
#print(numbers[0:5:-1])  #don't use negative values for step indexing because it will give you empty list

#different funtions for lists :----
numbers.append(7)      #first declear the function then print the list Append function add a number or string in the last of a list
print(numbers)
numbers.append("sahil")
print(numbers)
numbers.insert(2,9)  #insert function add a string or number after any index value first declear the index value and then add the number or stiring you wnat to add
numbers.remove("sahil")   #remove anything from the list
print(numbers)
x.pop()  # only removes the last digit from the list
print(x)


