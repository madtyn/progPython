"""
"""
from tkinter import mainloop, Button, X
from tkinter.messagebox import askyesno, showwarning, showinfo, showerror


def callback():
    '''
    Event handler
    '''
    if askyesno('Verify', 'Do you really want to quit?'):
        showwarning('Yes', 'Quit not yet implemented')
    else:
        showinfo('No', 'Quit has been cancelled')


errmsg = 'Sorry, no Spam allowed!'
Button(text='Quit', command=callback).pack(fill=X)
Button(text='Spam', command=(lambda: showerror('Spam', errmsg))).pack(fill=X)
mainloop()
