#In this we are adding radiobuttons in our elementpicker app
from tkinter import *
from random import choice,sample
wn = Tk()
wn["background"]= "white"
wn.title("Element Picker")

#from here our entry field is started
e = Entry(wn,background = "grey",foreground = "black",relief="sunken",width=25,borderwidth = 5)
e.grid(row = 0,column = 0,columnspan = 2,padx=50,pady=20)

#from here our radiobuttons will start:--
choise = IntVar()
rb1 = Radiobutton(wn,text="option 1",variable = choise,value =1)
rb2 = Radiobutton(wn,text="option 2",variable = choise,value =2)
rb1.grid(row =1,column=0,padx=50,pady=20 )
rb2.grid(row =1,column=1,padx=50,pady=20 )


#from here our functions will start:--
def show():
    lst = e.get().split(",")
    if choise.get()==2:
        ele = sample(lst,2)
        chois = "Choice: " + str(ele[0]+","+ele[1])
        msg=Label(wn,text=chois,background = "blue",foreground = "white",relief = "groove",width =20,borderwidth = 7)
        msg.grid(row =3,column=0,padx=50,pady=5,columnspan=2 )
    else:
        chois = "Choice: " + str(choice(lst))
        msg=Label(wn,text=chois,background = "blue",foreground = "white",relief = "groove",width =20,borderwidth = 7)
        msg.grid(row =3,column=0,padx=50,pady=5,columnspan=2 )
    if b1["state"] == DISABLED:
        b1["state"] = NORMAL

#from here our buttons will start :--
b = Button(wn,text = "Pick",command = show,background = "black",foreground = "white",relief = "sunken",borderwidth = 5)
b.grid(row = 2 ,column = 0,padx=30,pady=20)
b1 = Button(wn,text="Cancel",command = wn.quit,state = DISABLED,background = "red",foreground = "black",relief = "raised",borderwidth = 7)   
b1.grid(row = 2,column = 1,padx=10,pady=10)

wn.geometry("350x350")
wn.mainloop()