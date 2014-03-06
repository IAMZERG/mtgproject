##toying with the GUI tools... making program that enables one button when clicked, but disables itself.

from tkinter import *
import pickle

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master=None)
        self.pack()
        self.button1=Button(text="Button1")
        self.button2=Button(text="Button2")

        self.quit=Button(text="Quit")
        #binding click to the buttons
        self.button1.bind("<Button-1>", self.button2enable)
        self.button2.bind("<Button-1>", self.button1enable)
        self.quit.bind("<Button-1>", self.quitgame)
        #packing buttons onto frame
        self.button1.pack()
        self.button2.pack()
        self.quit.pack()

    #functions bound to buttons, frames, entries, etc. must be able to take event operator even if it isn't "used"
    def button2enable(self, event):
        self.button1.config(state=DISABLED)
        self.button2.config(state=NORMAL)
    def button1enable(self, event):
        self.button2.config(state=DISABLED)
        self.button1.config(state=NORMAL)
    def quitgame(self, event):
        root.destroy()

root=Tk()
frame=Frame(root)
win=Window(frame)
win.mainloop()

        

