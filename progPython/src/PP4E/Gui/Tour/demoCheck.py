"""
create a bar of check buttons that run dialog demos
"""
from tkinter import Frame, Label, Button, Checkbutton  # get base widget set
from tkinter import RIGHT, LEFT, X, BooleanVar
from dialogTable import demos  # get canned dialogs
from quitter import Quitter  # attach a quitter object to "me"


class Demo(Frame):
    '''
    Checkbuttons demo
    '''
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        self.tools()
        Label(self, text="Check demos").pack()
        self.vars = []
        for key in demos:
            var = BooleanVar()
            Checkbutton(self,
                        text=key,
                        variable=var,
                        command=demos[key]).pack(side=LEFT)
            self.vars.append(var)

    def report(self):
        '''
        Prints values in variables
        '''
        for var in self.vars:
            print(var.get(), end=' ')  # current toggle settings: 1 or 0
        print()

    def tools(self):
        '''
        Builds the buttons on the right
        '''
        frm = Frame(self)
        frm.pack(side=RIGHT)
        Button(frm, text='State', command=self.report).pack(fill=X)
        Quitter(frm).pack(fill=X)


if __name__ == '__main__':
    Demo().mainloop()
