from msilib.schema import Font
from tkinter import *
from datetime import datetime
app  = Tk()
app.geometry("250x200")
app.title("Age calculator")
app.configure(bg = "yellow")

msg = Label(app,text = "Enter your Date Of Birth",relief = "groove",background = "black",foreground = "white",borderwidth = 7,width = 20)
msg.grid(column = 0 , row = 0,columnspan=6)

dayl = Label(app,text = "Day: ")
monthl = Label(app,text = "Month: ")
yearl = Label(app,text = "Year: ")

       #Griding of different labels
daye = Entry(app,width = 2)
monthe = Entry(app,width = 2)
yeare = Entry(app,width = 4)
dayl.grid(row = 1,column = 0)
daye.grid(row = 1,column = 1)
monthl.grid(row = 1,column = 2)
monthe.grid(row = 1,column = 3)
yearl.grid(row = 1,column = 4)
yeare.grid(row = 1,column = 5)

       #defining functions:--
def find_sec():
    date = int(daye.get())
    mon = int(monthe.get())
    yr = int(yeare.get())
    dob = datetime(day = date,month = mon,year = yr)
    time1 = datetime.now()
    timediff = time1 - dob
    msg = Label(app,text = timediff.total_seconds())
    msg.grid(row = 3,column = 0,columnspan = 3)

def find_days():
    date = int(daye.get())
    mon = int(monthe.get())
    yr = int(yeare.get())
    dob = datetime(day = date,month = mon,year = yr)
    time1 = datetime.now()
    timediff = time1 - dob
    msg = Label(app,text = timediff)
    msg.grid(row = 3,column = 4,columnspan = 3)

b = Button(app,text="Total seconds",command = find_sec,background = "red",relief = "raised",borderwidth = 4)
b.grid(row = 2,column = 0,padx = 5,pady= 5)
b1 = Button(app,text="Total days",command = find_days,background = "red",relief = "raised",borderwidth = 4)
b.grid(row = 2,column = 0,columnspan=3)
b1.grid(row = 2,column = 4,columnspan=1)

app = mainloop()