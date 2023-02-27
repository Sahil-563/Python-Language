#changing the font and font size and adding colors in tk() window
from tkinter import *
from random import choice
wn = Tk()
wn["background"]= "white"
wn.title("Element Picker")
e = Entry(wn,background = "gray",foreground = "black")
e.grid(row = 0,column = 0,columnspan = 2,padx=50,pady=20)
def show():
    lst = e.get().split(",")
    chois = "Choice: " + str(choice(lst))
    msg=Label(wn,text=chois,font = ("bold",14),background = "black",foreground = "white")
    #here we are changing the font size of label or the msf which is going to be displayed in wn
    #background argument is used to change the color of the bakground
    #foreground argument is used to change the color of text
    msg.grid(row =2,column=0,padx=50,pady=5,columnspan=2 )
    if b1["state"] == DISABLED:
        b1["state"] = NORMAL

b = Button(wn,text = "Pick",command = show,background = "black",foreground = "white")
b.grid(row = 1 ,column = 0,padx=30,pady=20)
b1 = Button(wn,text="Cancel",command = wn.quit ,font = ("Couier",10) ,state = DISABLED,background = "red",foreground = "black")   
                                           #Here the state of cancel button is DISABLED
b1.grid(row = 1,column = 1,padx=10,pady=10)

wn.geometry("250x200")
wn.mainloop()