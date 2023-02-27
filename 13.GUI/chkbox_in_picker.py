#To randomly choose the two elements from the entry so we can use checkboxes
from tkinter import *
from random import choice,sample
wn = Tk()
wn["background"]= "white"
wn.title("Element Picker")

#from here our chekbutton will start:--
check = StringVar()
chk = Checkbutton(wn,text = "Double",variable = check,onvalue = "Checked",offvalue = "Unchecked", 
relief = "raised",background = "white",foreground="black",font =("bold",8))
chk.grid(row=1,column =0,padx=50,pady=20)
chk.deselect()

#getting our entry field from here in this field user will enter his or her data:--
e = Entry(wn,background = "grey",foreground = "black",relief="sunken",width=25,borderwidth = 5)
e.grid(row = 0,column = 0,columnspan = 2,padx=50,pady=20)

def show():
    lst = e.get().split(",")
    msg1 = Label(wn,text = check.get(),relief = "sunken",background = "black",foreground = "white")
    msg1.grid(row=1,column =1,padx=50,pady=20,columnspan=2)
    if check.get()=="Checked":
        ele = sample(lst,2)
        chois = "Choice: " +str(ele[0]+","+ele[1])
        msg=Label(wn,text=chois,background = "blue",foreground = "white",relief = "groove",width =20,borderwidth = 7) 
        msg.grid(row =3,column=0,padx=50,pady=5,columnspan=2 )
    else:
        chois = "Choice: "+str(choice(lst))
        msg=Label(wn,text=chois,background = "blue",foreground = "white",relief = "groove",width =20,borderwidth = 7) 
        msg.grid(row =3,column=0,padx=50,pady=5,columnspan=2 )
    if b1["state"] == DISABLED:
        b1["state"] = NORMAL

#from here our buttons will start:==
#1. Button for randomly picking the elements :==
b = Button(wn,text = "Pick",command = show,background = "black",foreground = "white",relief = "sunken",borderwidth = 5)
b.grid(row = 2 ,column = 0,padx=30,pady=20)
#button for quiting the tk window
b1 = Button(wn,text="Cancel",command = wn.quit,state = DISABLED,background = "red",foreground = "black",relief = "raised",borderwidth = 7)   
b1.grid(row = 2,column = 1,padx=10,pady=10)

wn.geometry("300x250")
wn.mainloop()