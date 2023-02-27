#slider in element picker:--
from tkinter import *
from random import choice ,sample
wn = Tk()
wn["background"]= "white"
wn.title("Element Picker")
e = Entry(wn,background = "grey",foreground = "black",relief="sunken",width=25,borderwidth = 5)
e.grid(row = 0,column = 0,columnspan = 2,padx=50,pady=20)

#from here our slider will start:--
var = IntVar()
sld = Scale(wn,from_=1,to=5,variable = var,orient = HORIZONTAL)
sld.grid(row = 1,column = 0,columnspan = 2,padx = 15,pady = 5)
def show():
    lst = e.get().split(",")
    if var.get() != 1:
        ele = sample(lst,var.get())
        lbl = ""
        for a in ele:
            lbl +=" "+a
            
        chois = "Choice: " + lbl
        msg=Label(wn,text=chois,background = "blue",foreground = "white",relief = "groove",width =20,borderwidth = 7)
        msg.grid(row =3,column=0,padx=50,pady=5,columnspan=2 )
    else:
        chois = "Choice: " + choice(lst)
        msg=Label(wn,text=chois,background = "blue",foreground = "white",relief = "groove",width =20,borderwidth = 7)
        msg.grid(row =3,column=0,padx=50,pady=5,columnspan=2 )

    if b1["state"] == DISABLED:
        b1["state"] = NORMAL

b = Button(wn,text = "Pick",command = show,background = "black",foreground = "white",relief = "sunken",borderwidth = 5)
b.grid(row = 2 ,column = 0,padx=30,pady=20)
b1 = Button(wn,text="Cancel",command = wn.quit,state = DISABLED,background = "red",foreground = "black",relief = "raised",borderwidth = 7)   
b1.grid(row = 2,column = 1,padx=10,pady=10)

wn.geometry("300x250")
wn.mainloop() 