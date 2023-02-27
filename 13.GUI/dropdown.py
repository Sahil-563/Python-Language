from tkinter import *
app = Tk()
app.geometry("200x200")
app.title("Drop_down_menu")
store = StringVar()
store.set("Colors")
lst = ["Green","Blue","Red"]
menu = OptionMenu(app,store,*lst)
menu.grid(row = 0,column = 0)
def show():
    msg = Label(app,text = store.get(),background = (store.get()).lower(),foreground = "black",font = ("bold",20),relief = "sunken")
    msg.grid(row = 2,column = 0)
b = Button(app,text = "show",command = show)
b.grid(row = 1,column = 0)
app.mainloop()