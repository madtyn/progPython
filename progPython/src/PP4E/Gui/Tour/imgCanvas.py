"""
    Canvas image example
"""
from tkinter import Tk, PhotoImage, Canvas, BOTH, NW

win = Tk()

GIFDIR = "../gifs/"
IMG = PhotoImage(file=GIFDIR + "ora-lp4e.gif")

can = Canvas(win)
can.pack(fill=BOTH)
can.create_image(2, 2, image=IMG, anchor=NW)  # x, y coordinates
win.mainloop()
