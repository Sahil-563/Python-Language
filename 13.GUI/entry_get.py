from tkinter import *
app = Tk()
app.geometry("310x200")
app.title("Entry")
e = Entry(app)   #This will take the entry from the user
e.pack()          #This will pack the entry object "e" in the app
def show():
    msg = Label(app,text = e.get())  #this wiil added to TK window once the button is pressed
    msg.pack()
b = Button(app,text = "Show",command = show)  #Now getting a entry entered by the user
b.pack()
app.mainloop()