"""
Frame examplePYTHON3

"""
# from sys import exit
from tkinter import Frame, Button  # get Tk widget classes
from tkinter import LEFT, RIGHT
from gui6 import Hello  # get the subframe class @UnresolvedImport

parent = Frame(None)  # make a container widget
parent.pack()
Hello(parent).pack(side=RIGHT)  # attach Hello instead of running it

Button(parent, text='Attach', command=exit).pack(side=LEFT)
parent.mainloop()
