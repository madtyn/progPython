"""
Frame example
"""
from tkinter import Frame, Button
from tkinter import LEFT


class Hello(Frame):  # an extended Frame
    '''
    Frame example
    '''
    def __init__(self, parent=None):
        Frame.__init__(self, parent)  # do superclass init
        self.pack()
        self.data = 42
        self.make_widgets()  # attach widgets to self

    def make_widgets(self):
        '''
        Makes the widgets in this frame
        '''
        widget = Button(self, text='Hello frame world!', command=self.message)
        widget.pack(side=LEFT)

    def message(self):
        '''
        Prints a message and updates the data counter
        '''
        self.data += 1
        print('Hello frame world %s!' % self.data)


if __name__ == '__main__':
    Hello().mainloop()
