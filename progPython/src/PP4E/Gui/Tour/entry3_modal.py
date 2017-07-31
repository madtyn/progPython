"""
    can fetch values after destroy with stringvars
"""
from tkinter import Tk, Toplevel, Button
from entry3 import makeform, fetch, FIELDS


def show(variables, popup):
    '''
    Shows the entries values and destroys the window
    :param variables: the variables
    :param popup: the dialog window
    '''
    popup.destroy()  # order doesn't matter here
    fetch(variables)  # variables live on after window destroyed


def ask():
    '''
    Creates the dialog and shows it as modal
    '''
    popup = Toplevel()  # show form in modal dialog window
    vars_ = makeform(popup, FIELDS)
    Button(popup, text='OK', command=(lambda: show(vars_, popup))).pack()
    popup.grab_set()
    popup.focus_set()
    popup.wait_window()  # wait for destroy here


root = Tk()
Button(root, text='Dialog', command=ask).pack()
root.mainloop()
