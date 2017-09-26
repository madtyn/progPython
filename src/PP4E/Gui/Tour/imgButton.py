"""
    Image example
"""
from tkinter import Tk, PhotoImage, Button

win = Tk()

GIFDIR = "../gifs/"
IGM = PhotoImage(file=GIFDIR + "ora-pp.gif")

Button(win, image=IGM).pack()
win.mainloop()
