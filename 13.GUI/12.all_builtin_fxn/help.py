#help function is used to get the information about the a function Everything in a doc string is printed when help function is called
def greet(name):
    """This is a function which is used to greet a user"""
    print(f"have a nice day {name}")
print(help(greet))
