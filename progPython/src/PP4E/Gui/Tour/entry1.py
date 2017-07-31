"""
    Entry example
"""
from tkinter import Tk, Entry, Button
from tkinter import TOP, X, LEFT, RIGHT
from quitter import Quitter


def fetch():
    '''
    Prints the Entry content
    '''
    print('Input => "%s"' % ent.get())  # get text


root = Tk()
ent = Entry(root)
ent.insert(0, 'Type words here')  # set text
ent.pack(side=TOP, fill=X)  # grow horiz

ent.focus()  # save a click
ent.bind('<Return>', (lambda __: fetch()))  # on enter key
btn = Button(root, text='Fetch', command=fetch)  # and on button
btn.pack(side=LEFT)
Quitter(root).pack(side=RIGHT)
root.mainloop()
