import tkinter
from tkinter import *
app=Tk()
app.geometry("300x250")
app.title("Calculator")
app.configure(bg = "blue")

e = Entry(app,width = 30)

def add_buttons(char):
    #e.delete(0, number)
    e.insert(0,char)
def ans():
    pass

#Our basix 10 buttons:--   
b1 = Button(app,text="1",command = lambda:add_buttons(1),width = 5)
b2 = Button(app,text="2",command = lambda:add_buttons(2),width= 5)
b3 = Button(app,text="3",command = lambda:add_buttons(3),width= 5)
b4 = Button(app,text="4",command = lambda:add_buttons(4),width= 5)
b5 = Button(app,text="5",command = lambda:add_buttons(5),width= 5)
b6 = Button(app,text="6",command = lambda:add_buttons(6),width= 5)
b7 = Button(app,text="7",command = lambda:add_buttons(7),width= 5)
b8 = Button(app,text="8",command = lambda:add_buttons(8),width= 5)
b9 = Button(app,text="9",command = lambda:add_buttons(9),width= 5)
b0 = Button(app,text="0",command = lambda:add_buttons(0),width= 5)

#equal to and cancel button
equals = Button(app,text="=",command = ans,width= 5)
cancel = Button(app,text="Cancel",command = app.quit,width= 5)

#operator buttons:--
opb1 = Button(app,text = "+",command = lambda:add_buttons("+"))
opb2 = Button(app,text = "-",command = lambda:add_buttons("-"))
opb3 = Button(app,text = "/",command = lambda:add_buttons("/"))
opb4 = Button(app,text = "*",command = lambda:add_buttons("*"))


#griding of buttons:--
e.grid(row =0 ,column=0,padx=15,pady=10,columnspan=3)
b1.grid(row = 1,column=0,padx=15,pady=10)
b2.grid(row = 1,column=1,padx=15,pady=10)
b3.grid(row = 1,column=2,padx=15,pady=10)
b4.grid(row = 2,column=0,padx=15,pady=10)
b5.grid(row = 2,column=1,padx=15,pady=10)
b6.grid(row = 2,column=2,padx=15,pady=10)
b7.grid(row = 3,column=0,padx=15,pady=10)
b8.grid(row = 3,column=1,padx=15,pady=10)
b9.grid(row = 3,column=2,padx=15,pady=10)
b0.grid(row = 4,column=0,padx=15,pady=10)
opb1.grid(row=1,column = 5,padx = 15,pady = 10)
opb2.grid(row=2,column = 5,padx = 15,pady = 10)
opb3.grid(row=3,column = 5,padx = 15,pady = 10)
opb4.grid(row=4,column = 5,padx = 15,pady = 10)
equals.grid(row = 4,column = 1,padx=15,pady=15)
cancel.grid(row = 4,column = 2,padx=15,pady=15)


app.mainloop()