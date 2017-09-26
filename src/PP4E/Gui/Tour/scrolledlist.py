"a simple customizable scrolled listbox component"

from tkinter import Frame, Listbox, Scrollbar
from tkinter import Y, YES, BOTH, LEFT, RIGHT, SUNKEN


class ScrolledList(Frame):
    def __init__(self, options_, parent=None):
        # do superclass init
        super().__init__(parent)  # Same as super(__class__, self, parent) and
                                  # Frame.__init__(self, parent) from Python 2.x
        self.pack(expand=YES, fill=BOTH)                   # make me expandable
        self.makeWidgets(options_)

    def handleList(self, event):
        index = self.listbox.curselection()                # on list double-click
        label = self.listbox.get(index)                    # fetch selection text
        self.runCommand(label)                             # and call action here
                                                           # or get(ACTIVE)

    def makeWidgets(self, options_):
        labList = Listbox(self, relief=SUNKEN)
        sbar = Scrollbar(self)
        sbar.config(command=labList.yview)                    # xlink sbar and list
        labList.config(yscrollcommand=sbar.set)               # move one moves other
        sbar.pack(side=RIGHT, fill=Y)                         # pack first=clip last
        labList.pack(side=LEFT, expand=YES, fill=BOTH)        # list clipped first
        pos = 0
        for label in options_:                                 # add to listbox
            labList.insert(pos, label)                        # or insert(END,label)
            pos += 1                                          # or enumerate(options)
        #list.config(selectmode=SINGLE, setgrid=1)            # select,resize modes
        labList.bind('<Double-1>', self.handleList)           # set event handler
        self.listbox = labList

    @staticmethod
    def runCommand(selection):                       # redefine me lower
        print('You selected:', selection)


if __name__ == '__main__':
    options = (('Lumberjack-%s' % x) for x in range(20))  # or map/lambda, [...]
    ScrolledList(options).mainloop()
