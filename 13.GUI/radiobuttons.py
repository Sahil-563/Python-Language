#Radiobuttons are used to creaate two options for the user:--
from tkinter import *
app = Tk()
app.geometry("200x100")
app.title("Radio buttons")

choice = IntVar()
rb1 = Radiobutton(app,text = "option1",variable = choice,value = 1 )
rb2 = Radiobutton(app,text = "option2",variable = choice,value = 2)
rb1.pack()
rb2.pack()

def show():
    msg = Label(app,text = choice.get())
    msg.pack()

b = Button(app,text = "show",command = show)
b.pack()
app.mainloop()