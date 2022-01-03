from tkinter import *

def destroy():
    button.destroy()


root = Tk()

root.geometry("200x200")

button = Button(root , text = 'Close the window' , command = destroy)
button.pack(pady = 10)

root.mainloop()

