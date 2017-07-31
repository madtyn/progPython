"""
use Entry widgets directly
lay out by rows with fixed-width labels: this and grid are best for forms
"""

from tkinter import Tk, Button, Frame, Label, Entry
from tkinter import TOP, LEFT, RIGHT, YES, X
from quitter import Quitter
FIELDS = 'Name', 'Job', 'Pay'


def fetch(entries):
    '''
    Prints the received entries
    :param entries:the entries
    '''
    for entry in entries:
        print('Input => "%s"' % entry.get())  # get text


def makeform(parent, fields):
    '''
    Builds the form
    :param parent: the root
    :param fields: the field names
    '''
    entries = []
    for field in fields:
        row = Frame(parent)  # make a new row
        lab = Label(row, width=5, text=field)  # add label, entry
        ent = Entry(row)
        row.pack(side=TOP, fill=X)  # pack row on top
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)  # grow horizontal
        entries.append(ent)
    return entries


if __name__ == '__main__':
    root = Tk()
    ents = makeform(root, FIELDS)
    root.bind('<Return>', (lambda __: fetch(ents)))
    Button(root, text='Fetch',
           command=(lambda: fetch(ents))).pack(side=LEFT)
    Quitter(root).pack(side=RIGHT)
    root.mainloop()
