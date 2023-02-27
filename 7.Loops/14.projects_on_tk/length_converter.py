from tkinter import *
app = Tk()
app.geometry("277x145")
app.configure(bg = "cyan")
app.title("Length Converter")

msg = Label(app,text = "Enter the value:",background = "black",foreground = "red",font = ("bold",10) )
msg.grid(row=0,column = 0,columnspan = 1)
e = Entry(app,relief = "sunken",borderwidth = 3,background = "black",foreground = "yellow")
e.grid(row = 0,column = 1,columnspan = 2)

scales = ["Centimeter","Meter","Killometer"]
_from = StringVar()
_from.set("Scale")
from_menu = OptionMenu(app,_from,*scales)
from_menu.grid(row = 1,column = 0,pady = 10)
from_menu.config(bg = "black")
from_menu.config(fg = "red")

msg = Label(app,text = "Convert to",background = "black",foreground = "yellow")
msg.grid(row = 1,column = 1,pady = 10)

_to = StringVar()
_to.set("Scale")
to_menu = OptionMenu(app,_to,*scales)
to_menu.grid(row = 1,column = 2,pady = 10,padx = 3)
to_menu.config(bg = "black")
to_menu.config(fg = "red")
def convert():
    scale1 = _from.get() 
    scale2 = _to.get()
    num = e.get()
    num = int(num)
    if scale1 == "Centimeter" and scale2 == "Meter":
        res = num/100
    elif scale1 == "Centimeter" and scale2 == "Killometer":
        res = num/100000
    elif scale1 == "Meter" and scale2 == "Centimeter":
        res = num*100
    elif scale1 == "Meter" and scale2 == "Killometer":
        res = num/1000
    elif scale1 == "Killometer" and scale2 == "Centimeter":
        res = num*100000
    elif scale1 == "Killometer" and scale2 == "Meter":
        res = num*1000
    else:
        res = num
    msg = Label(app,text = res,background = "black",foreground = "yellow")
    msg.grid(row = 3,column = 1 ,pady = 15)


msg = Label(app,text = "Result: ",background = "black",foreground = "red",font = ("bold",10))
msg.grid(row = 3,column = 0,pady =15)
b = Button(app,text = "Convert",command = convert,relief = "raised",borderwidth=3,background = "black",foreground = "red")
b.grid(row =2,column = 1)

app.mainloop()
