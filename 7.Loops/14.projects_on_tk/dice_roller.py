from tkinter import *
dice={0 : "🎲",
1 : "⚀",
2 : "⚁",
3 : "⚂",
4 : "⚃",
5 : "⚄",
6 : "⚅"}
app = Tk()
app.configure(bg="silver")
app.title("Dice_roller")
app.geometry("200x250")
msg = Label(app,text=dice[0],font=("bold",100))
msg.grid(row =0,column = 0,columnspan = 2,padx=30,pady=10)

def roll():
    from random import randint
    num = randint(1,6)
    msg = Label(app,text=dice[num],font=("bold",100))
    msg.grid(row =0,padx=25,pady=10,columnspan = 2)
    if close["state"] == DISABLED:
        close["state"] = NORMAL
roll_button=Button(app,text = "Roll",command = roll,relief = "raised",background = "grey",foreground = "black",borderwidth=7,font =("bold",10))
roll_button.grid(row = 1,column = 0,padx = 25,pady=10)
close = Button(app,text = "Close",command = app.quit,state = DISABLED,relief = "raised",background = "red",foreground = "black",borderwidth=7,font =("bold",10))
close.grid(row = 1,column = 1,padx = 25,pady=10)
app.mainloop()
