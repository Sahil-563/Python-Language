#Toplevel is used to create different windows for different outputs
from tkinter import *
from random import choice
wn = Tk()
wn.title("grid method")
e = Entry(wn)
e.grid(row = 0,column = 0,columnspan = 2,padx=50,pady=20)
def show():
    lst = e.get().split(",")
    chois = "Choice: " + str(choice(lst))
    #From here our new window will start
    wn2 = Toplevel()
    wn2.title("New_window")

    msg=Label(wn2,text=chois)
    msg.grid(row =2,column=0,padx=10,pady=5 )
b = Button(wn,text = "pick",command = show)
b.grid(row = 1 ,column = 0,padx=30,pady=20)
b1 = Button(wn,text="cancel",command = wn.quit)
b1.grid(row = 1,column = 1,padx=10,pady=10)

wn.geometry("250x200")
wn.mainloop()