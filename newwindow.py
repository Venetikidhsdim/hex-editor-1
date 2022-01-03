from tkinter import *
from tkinter.ttk import *

master = Tk()

master.geometry("200x200")

def openNewWindow():

    newWindow = Toplevel(master)

    newWindow.title(" New Window")

    newWindow.geometry("200x200")

    Label(newWindow , text = "New Window").pack()



label = Label(master , text = "main window")

label.pack(pady = 10)

btn = Button(master , text = "Click to open a new window" , command = openNewWindow)

btn.pack(pady = 10)

mainloop()
    
