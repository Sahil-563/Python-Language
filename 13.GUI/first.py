import tkinter
from tkinter import *
app = Tk()  #it is like a window for the gui 
app.title("App")  #It is used to give the title for the GUI window
app.geometry("200x100")  #It i is used to set the size of the window
text = Label(app,text="First GUI interface")   #It is used to add text inside our GUI window
text.pack()  #used to pack the text in window
app.mainloop()  #used to run the GUI window
