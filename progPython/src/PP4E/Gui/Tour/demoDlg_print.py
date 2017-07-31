"""
similar, but show return values of dialog calls;  the lambda saves data from
the local scope to be passed to the handler (button press handlers normally
get no arguments, and enclosing scope references don't work for loop variables)
and works just like a nested def statement: def func(key=key): self.printit(key)
"""

from tkinter import Frame, Label, Button, TOP, BOTH  # get base widget set
from dialogTable import demos  # button callback handlers
from quitter import Quitter  # attach a quit object to me


class Demo(Frame):
    '''
    Demo for dialogs
    '''
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        Label(self, text="Basic demos").pack()
        for key in demos:
            func = (lambda key=key: self.printit(key))
            Button(self, text=key, command=func).pack(side=TOP, fill=BOTH)
        Quitter(self).pack(side=TOP, fill=BOTH)

    def printit(self, name):
        '''
        Prints the result of executing a recovered function
        :param name: a string to be printed
        '''
        print(name, 'returns =>', demos[name]())  # fetch, call, print


if __name__ == '__main__':
    Demo().mainloop()
