from tkinter import *
from random import choice 
app = Tk()
app.geometry("400x350")
app.title("Element picker")
msg = Label(app,text="Good Morning\nPlease enter the name of fruits comma separately:--")
msg.pack()
e = Entry(app)
e.pack()
msg = Label(app,text = "Click to choose one fruit")
msg.pack()

def pick():
    lst = e.get().split(",")   #It will split the entered elements which are in the form of string in a list
    msg = Label(app,text=choice(lst))  #The choice function will choose randomly any ele from the list
    msg.pack()
b = Button(app,text ="Pick",command =pick)
b.pack()
app.mainloop()