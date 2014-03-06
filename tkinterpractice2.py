##this shows how to create Entry objects, StringVar objects, and
##how to disable them, and how to "bind" actions to them.
from tkinter import *
import mtgmainfile

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

        self.variablebox = Entry()
        self.button = Button(text="this is a button")
        self.button.bind('<Button-1>', self.enable_button)
        self.button.pack()
        self.variablebox.pack()

        # here is the application variable
        self.contents = StringVar()
        # set it to some value
        self.contents.set("")
        # tell the entry widget to watch this variable
        self.variablebox["textvariable"] = self.contents

        # and here we get a callback when the user hits return.
        # we will have the program print out the value of the
        # application variable when the user hits return
        self.variablebox.bind('<Key-Return>',
                              self.print_and_reset_contents)

    def print_and_reset_contents(self, event):
        print ("hi. contents of entry is now ---->", \
              self.contents.get())
        self.variablebox.config(state=DISABLED)
    def enable_button(self, event):
        self.variablebox.config(state=NORMAL)


win=Tk()
frame=Frame(win)
window=App(frame)
window.mainloop()



