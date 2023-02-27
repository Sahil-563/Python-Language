   #showing a string a palidrome or not

string = input("Enter a string: ")
original_str = string.lower()   
string1 = original_str[::-1]  #this is step argument which will reverse the string
if original_str == string1:
    print(f"The string {string} is a palidrome string")
else:
    print(f"The string {string} is not a palidrome string")