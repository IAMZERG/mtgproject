from tkinter import *

def makebutton(win, frame):
    newbutton=Button(win, text="this is a button", command=makebutton(win, frame))
    newbutton.grid()


win=Tk()
frame=Frame(win)
button=Button(win, text="this is a button", command=makebutton(win, frame))
button.grid()
title="title"
win.title(title)
win.mainloop()



