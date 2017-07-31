"""
    Simple scale widget example
"""
from tkinter import Tk, Scale, Button
from tkinter import RIGHT, YES, Y


root = Tk()
scl = Scale(root, from_=-100, to=100, tickinterval=50, resolution=10)
scl.pack(expand=YES, fill=Y)


def report():
    '''
    Prints value
    '''
    print(scl.get())


Button(root, text='state', command=report).pack(side=RIGHT)
root.mainloop()
