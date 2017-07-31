"""
a Quit button that verifies exit requests;
to reuse, attach an instance to other GUIs, and re-pack as desired
"""
from tkinter import Frame, Button  # get widget classes
from tkinter import LEFT, YES, BOTH
from tkinter.messagebox import askokcancel  # get canned std dialog


class Quitter(Frame):  # subclass our GUI
    '''
    A smart quit Button
    '''
    def __init__(self, parent=None):  # constructor method
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='Quit', command=self.quit)
        widget.pack(side=LEFT, expand=YES, fill=BOTH)

    def quit(self):
        ans = askokcancel('Verify exit', "Really quit?")
        if ans:
            Frame.quit(self)


if __name__ == '__main__':
    Quitter().mainloop()
