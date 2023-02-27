import tkinter
from tkinter import *
app = Tk()
app.title("For Fun")
app.geometry("210x200")
def wish():
    msg = Label(app,text = "Good morning")
    msg.pack()
b = Button(app,text="Click",command=wish)    #command always takes a function 
b.pack()
     
     #creating two buttons in single GUI window
     #2nd is for generating random numbers by clicking on a single button
from random import randint
def random_num():
    num = Label(app,text = randint(1,100))
    num.pack()
b = Button(app,text="Generate",command = random_num)
b.pack()
      
          #button to close the Tk() window
quitb = Button(app,text = "Close",command= app.quit())
app.mainloop()
