"""
check and radio button bar classes for apps that fetch state later;
pass a list of options, call state(), variable details automated
"""

from tkinter import Tk, Frame, Button, Radiobutton, Checkbutton, IntVar, StringVar
from tkinter import YES, LEFT, RIGHT, TOP, GROOVE, RIDGE, W, X, Y, NW


class Checkbar(Frame):
    '''
    Checkbar reusable component
    '''
    def __init__(self, parent=None, picks=None, side=LEFT, anchor=W):
        '''
        Constructor
        :param parent: the parent
        :param picks:
        :param side: the side to pack to
        :param anchor: the location
        '''
        if not picks:
            picks = []
        Frame.__init__(self, parent)
        self.vars = []
        for pick in picks:
            var = IntVar()
            chk = Checkbutton(self, text=pick, variable=var)
            chk.pack(side=side, anchor=anchor, expand=YES)
            self.vars.append(var)

    def state(self):
        '''
        Returns state
        '''
        return [var.get() for var in self.vars]


class Radiobar(Frame):
    '''
    Radiobar reusable component
    '''
    def __init__(self, parent=None, picks=None, side=LEFT, anchor=W):
        '''
        Constructor
        :param parent: the parent
        :param picks:
        :param side: the side to pack to
        :param anchor: the location
        '''
        if not picks:
            picks = []
        Frame.__init__(self, parent)
        self.var = StringVar()
        self.var.set(picks[0])
        for pick in picks:
            rad = Radiobutton(self, text=pick, value=pick, variable=self.var)
            rad.pack(side=side, anchor=anchor, expand=YES)

    def state(self):
        '''
        Returns state
        '''
        return self.var.get()


if __name__ == '__main__':
    root = Tk()
    lng = Checkbar(root, ['Python', 'C#', 'Java', 'C++'])
    gui = Radiobar(root, ['win', 'x11', 'mac'], side=TOP, anchor=NW)
    tgl = Checkbar(root, ['All'])

    gui.pack(side=LEFT, fill=Y)
    lng.pack(side=TOP, fill=X)
    tgl.pack(side=LEFT)
    lng.config(relief=GROOVE, bd=2)
    gui.config(relief=RIDGE, bd=2)

    def allstates():
        '''
        Prints all states
        '''
        print(gui.state(), lng.state(), tgl.state())

    from quitter import Quitter
    Quitter(root).pack(side=RIGHT)
    Button(root, text='Peek', command=allstates).pack(side=RIGHT)
    root.mainloop()
