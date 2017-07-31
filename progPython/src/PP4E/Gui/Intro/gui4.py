from tkinter import Frame, Label, Button
from tkinter import TOP, YES, BOTH, LEFT, RIGHT, X, Y


def greeting():
    '''
    Prints a greeting
    '''
    print('Hello stdout world!...')


win = Frame()
win.pack(side=TOP, expand=YES, fill=BOTH)
Label(win, text='Hello container world').pack(side=TOP)
Button(win, text='Hello', command=greeting).pack(side=LEFT, fill=Y)
Button(win, text='Quit', command=win.quit).pack(side=RIGHT, expand=YES, fill=X)

win.mainloop()
