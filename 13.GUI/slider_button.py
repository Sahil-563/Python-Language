#slider widgets are used to create wide range of selection using one button
#To create slider buttons we us scale()class
from distutils import command
from tkinter import *
wn = Tk()
wn.title("Slider_buttons")
wn.geometry("220x200")

#from here our slider widget will start:-         
var = IntVar()  #scale class can only have integer as variable not string 
sld = Scale(wn,from_=0,to=100,variable = var,orient = HORIZONTAL,relief = "sunken",background = "black",foreground = "blue") 
                #in this we have to give two parameters from where the scale will start and to where scale will end
                #now by default our slider will be verticle so we can change its orientation using orient paramter
sld.pack()

def show():
    msg = Label(wn,text = var.get())
    msg.pack()
b = Button(wn,text = "show",command = show)
b.pack()

wn.mainloop()