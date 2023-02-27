#open a text file in python using open keyword and passsing file name as attribute in open()
txt=open("text.txt",mode='r')   #passed a filename as an attribute in open()
print(txt.read())      #.read() method is used to read what is inside in a file
txt1 = open("text.txt",mode="w")  #by "w" mode you can write and change the text in a file
txt1.write("fuck you RiruRaj again")  #.write() method is used to write in a file
txt1=open("text.txt",mode="r")     #when you have modified a file you have to call mode="r"
print(txt1.read())                 #used to read a file
txt1 = open("text.txt",mode = "a")   #mode="a" is used to append new text in file
txt1.write("\nYou are bad pussy")
#txt1 = open("text.txt",mode = "r")
print(txt1.read())