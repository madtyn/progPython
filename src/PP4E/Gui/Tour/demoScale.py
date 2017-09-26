"""
create two linked scales used to launch dialog demos
"""
from tkinter import Frame, Label, Button, Scale, IntVar  # get base widget set
from tkinter import YES, LEFT, RIGHT

from dialogTable import demos  # button callback handlers
from quitter import Quitter  # attach a quit frame to me


class Demo(Frame):
    '''
    Scales example
    '''
    def __init__(self, parent=None, **options):
        '''
        Constructor
        :param parent: the parent
        '''
        Frame.__init__(self, parent, **options)
        self.pack()
        Label(self, text="Scale demos").pack()
        self.var = IntVar()
        Scale(self, label='Pick demo number',
              command=self.onMove,  # catch moves
              variable=self.var,  # reflects position
              from_=0, to=len(demos) - 1).pack()
        Scale(self, label='Pick demo number',
              command=self.onMove,  # catch moves
              variable=self.var,  # reflects position
              from_=0, to=len(demos) - 1,
              length=200, tickinterval=1,
              showvalue=YES, orient='horizontal').pack()
        Quitter(self).pack(side=RIGHT)
        Button(self, text="Run demo", command=self.onRun).pack(side=LEFT)
        Button(self, text="State", command=self.report).pack(side=RIGHT)

    def onMove(self, value):
        '''
        Movement handler
        :param value: the current value
        '''
        print('in onMove', value)

    def onRun(self):
        '''
        Selection handler
        '''
        pos = self.var.get()
        print('You picked', pos)
        demo = list(demos.values())[pos]  # map from position to value (3.X view)
        print(demo())  # or demos[ list(demos.keys())[pos] ]()

    def report(self):
        '''
        Prints value
        '''
        print(self.var.get())


if __name__ == '__main__':
    print(list(demos.keys()))
    Demo().mainloop()
