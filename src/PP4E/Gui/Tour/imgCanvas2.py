"""
    Canvas image example 2
"""
from sys import argv
from tkinter import Tk, Canvas, PhotoImage, BOTH, NW

win = Tk()

GIFDIR = "../gifs/"
FILENAME = argv[1] if len(argv) > 1 else 'ora-lp4e.gif'  # name on cmdline?
IMG = PhotoImage(file=GIFDIR + FILENAME)

can = Canvas(win)
can.pack(fill=BOTH)
can.config(width=IMG.width(), height=IMG.height())  # size to IMG size
can.create_image(2, 2, image=IMG, anchor=NW)
win.mainloop()
