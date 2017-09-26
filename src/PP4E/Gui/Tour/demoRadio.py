"""
    create a group of radio buttons that launch dialog demos

"""

from tkinter import Frame, Label, Button, Radiobutton, StringVar  # get base widget set
from tkinter import TOP, NW, X
from dialogTable import demos  # button callback handlers
from quitter import Quitter  # attach a quit object to "me"


class Demo(Frame):
    '''
    Radiobutton demo
    '''
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        Label(self, text="Radio demos").pack(side=TOP)
        self.var = StringVar()
        for key in demos:
            Radiobutton(self, text=key,
                        command=self.onPress,
                        variable=self.var,
                        value=key).pack(anchor=NW)
        self.var.set(key)  # select last to start pylint: disable=undefined-loop-variable
        Button(self, text='State', command=self.report).pack(fill=X)
        Quitter(self).pack(fill=X)

    def onPress(self):
        '''
        Press handler
        '''
        pick = self.var.get()
        print('you pressed', pick)
        print('result:', demos[pick]())

    def report(self):
        '''
        Prints selected value
        '''
        print(self.var.get())


if __name__ == '__main__':
    Demo().mainloop()
