def result(name=None,num=None):          #Here we have passed a parameter to an argument
    if name != None or num != None:
        print(f"Name:{name}")
        print(f"Marks:{num}")

result(num=44)    #Now it will not show error because we have passed a parameter in an argument