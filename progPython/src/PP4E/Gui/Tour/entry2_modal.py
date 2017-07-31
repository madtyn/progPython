"""
make form dialog modal; must fetch before destroy with entries
"""

from tkinter import Tk, Toplevel, Button
from entry2 import makeform, fetch, FIELDS


def show(entries, popup):
    '''
    Shows the entries values and destroys the window
    :param entries: the entries
    :param popup: the dialog window
    '''
    fetch(entries)  # must fetch before window destroyed!
    popup.destroy()  # fails with msgs if stmt order is reversed


def ask():
    '''
    Creates the dialog and shows it as modal
    '''
    popup = Toplevel()  # show form in modal dialog window
    ents = makeform(popup, FIELDS)
    Button(popup, text='OK', command=(lambda: show(ents, popup))).pack()
    popup.grab_set()
    popup.focus_set()
    popup.wait_window()  # wait for destroy here


root = Tk()
Button(root, text='Dialog', command=ask).pack()
root.mainloop()
