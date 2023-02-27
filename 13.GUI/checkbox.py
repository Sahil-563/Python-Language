#Checkbutton is used to create checkboxes in tkinter

from tkinter import *
app = Tk()
app.geometry("200x150")
app.title("Checkbox")
check =  StringVar()
chk = Checkbutton(app,variable = check,onvalue = "Selected",offvalue = "Deselected") #onvalue is used to show that 
                                                                                     #the chekbox is selected
                                                                                     #offvalue is used to show
                                                                                     #that the checkbox is deselectede
                                                                                            
chk.deselect()   #if we introduce onvalue parameter then the checkbox is always selected from starting so we have to deselect that
chk.grid(row=0,column=0,padx = 25,pady = 10)
b = Button(app,text = "cancel",command = app.quit)
b.grid(row=1,column = 1,padx = 25,pady = 0)
def show():
    msg = Label(app,text = check.get())
    msg.grid(row = 2,column = 0,padx = 25,pady = 10)
b1 = Button(app,text = "Show",command = show)
b1.grid(row=1,column = 0,padx = 25,pady = 10)

app.mainloop()