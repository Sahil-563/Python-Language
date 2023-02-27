#print():-- This is used to print a specific text with different escapse sequences
print(1,2,3,sep="___")  #sep keyword is used to seperate the text or integers by what we had passed in sep
print("Sahil","Vishal","Nobody",sep="\n")
   #use of end
print("what is your name? ",end = "")
print("Rekha")
       
       #opening a file and printing inside a file
x = open("text.txt",mode = 'w')
x = open("text.txt",mode = 'a')
x.write("Sahl is Akshita's bestfrind\n")
print("you are doing well Akshita",file = x)
x = open("text.txt",mode = "r")
print(x.read())
