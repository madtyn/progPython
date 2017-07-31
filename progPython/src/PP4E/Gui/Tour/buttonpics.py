"""
    Button pics example
"""
import random  # pick a picture at random
from tkinter import Frame, Label, Button, PhotoImage  # get base widget set
from tkinter import BOTH, SUNKEN
from glob import glob  # filename expansion list
import demoCheck  # attach check button example to me

GIFDIR = '../gifs/'  # default dir to load GIF files


class ButtonPicsDemo(Frame):  # pylint: disable=too-many-ancestors
    '''
    ButtonPicsDemo class
    '''
    def __init__(self, gifdir=GIFDIR, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.lbl = Label(self, text="none", bg='blue', fg='red')
        self.pix = Button(self, text="Press me", command=self.draw, bg='white')

        self.lbl.pack(fill=BOTH)
        self.pix.pack(pady=10)

        demoCheck.Demo(self, relief=SUNKEN, bd=2).pack(fill=BOTH)
        files = glob(gifdir + "*.gif")
        print(files)
        self.images = [(x, PhotoImage(file=x)) for x in files]

    def draw(self):
        '''
        Draw a new pic on the button
        '''
        name, photo = random.choice(self.images)
        self.lbl.config(text=name)
        self.pix.config(image=photo)


if __name__ == '__main__':
    ButtonPicsDemo().mainloop()
