#Question:---Calculate the factors of a given number entered by a user:---

x=int(input("Enter a number to calculate it's factors"))
print(f"The factors of {x}: ")
for ele in range(1,x+1):
    if x%ele==0:
        print(ele)



