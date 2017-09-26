from tkinter import Frame, Button  # get Tk widget classes
from tkinter import LEFT, RIGHT
from gui6 import Hello  # get the subframe class @UnresolvedImport


class HelloContainer(Frame):
    '''
    The Hello Container
    '''
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.makeWidgets()

    def makeWidgets(self):
        '''
        Makes the widgets
        '''
        Hello(self).pack(side=RIGHT)  # attach a Hello to me
        Button(self, text='Attach', command=self.quit).pack(side=LEFT)


if __name__ == '__main__':
    HelloContainer().mainloop()
