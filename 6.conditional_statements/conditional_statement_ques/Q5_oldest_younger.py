"""Question:----
           Take input of age of 3 people by user and determine the oldest and youngest among them """

name_1=input("Enter your name: ")
age_1=int(input("Enter your age: "))

name_2=input("Enter your name: ")
age_2=int(input("Enter your age: "))

name_3=input("Enter your name: ")
age_3=int(input("Enter your age: "))

if age_1>age_2 and age_1>age_3:
    print(f"The oldest among three is: {name_1}")
elif age_1<age_2 and age_1<age_3:
    print(f"The youngest among three is: {name_1}")
if age_2>age_1 and age_2>age_3:
    print(f"The oldest among three is: {name_2}")
elif age_2<age_1 and age_2<age_3:
    print(f"The youngest among three is: {name_2}")
if age_3>age_1 and age_3>age_2:
    print(f"The oldest among three is: {name_3}")
elif age_3<age_1 and age_3<age_1:
    print(f"The youngest among three is: {name_3}")


    
