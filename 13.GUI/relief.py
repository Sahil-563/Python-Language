#relief parameter is used to change a normal messsage into a form of button which can be flatened as well as raised
from tkinter import *
from random import choice
wn = Tk()
wn["background"]= "white"
wn.title("Element Picker")
e = Entry(wn,background = "grey",foreground = "black",relief="sunken",width=25,borderwidth = 5)
e.grid(row = 0,column = 0,columnspan = 2,padx=50,pady=20)
def show():
    lst = e.get().split(",")
    chois = "Choice: " + str(choice(lst))
    msg=Label(wn,text=chois,background = "blue",foreground = "white",relief = "groove",width =20,borderwidth = 7) #Now it will be rsised as button
    msg.grid(row =2,column=0,padx=50,pady=5,columnspan=2 )
    if b1["state"] == DISABLED:
        b1["state"] = NORMAL

b = Button(wn,text = "Pick",command = show,background = "black",foreground = "white",relief = "sunken",borderwidth = 5)
b.grid(row = 1 ,column = 0,padx=30,pady=20)
b1 = Button(wn,text="Cancel",command = wn.quit,state = DISABLED,background = "red",foreground = "black",relief = "raised",borderwidth = 7)   
b1.grid(row = 1,column = 1,padx=10,pady=10)

wn.geometry("250x200")
wn.mainloop()