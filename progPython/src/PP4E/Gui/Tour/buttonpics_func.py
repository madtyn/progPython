"""
    Buttons with pictures example
"""
from tkinter import Tk, Label, Button, PhotoImage  # get base widget set
from tkinter import BOTH, SUNKEN
from glob import glob  # filename expansion list
import random  # pick a picture at random
import demoCheck  # attach checkbutton demo to me


def draw():
    '''
    Draws
    '''
    name, photo = random.choice(IMAGES)
    lbl.config(text=name)
    pix.config(image=photo)


root = Tk()

GIFDIR = '../gifs/'  # where to look for GIF FILES
FILES = glob(GIFDIR + "*.gif")  # GIFs for now
IMAGES = [(x, PhotoImage(file=x)) for x in FILES]  # load and hold

lbl = Label(root, text="none", bg='blue', fg='red')
pix = Button(root, text="Press me", command=draw, bg='white')
lbl.pack(fill=BOTH)
pix.pack(pady=10)
demoCheck.Demo(root, relief=SUNKEN, bd=2).pack(fill=BOTH)
print(FILES)
root.mainloop()
