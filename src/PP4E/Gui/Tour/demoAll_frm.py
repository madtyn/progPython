"""
4 demo class components (subframes) on one window;
there are 5 Quitter buttons on this one window too, and each kills entire gui;
GUIs can be reused as frames in container, independent windows, or processes;
"""

from tkinter import Tk, Label, Button
from tkinter import YES, LEFT, BOTH, GROOVE, X
from quitter import Quitter


demoModules = ['demoDlg', 'demoCheck', 'demoRadio', 'demoScale']
parts = []


def addComponents(root):
    '''
    Adds components
    :param root: the parent
    '''
    for demo in demoModules:
        module = __import__(demo)  # import by name string
        part = module.Demo(root)  # attach an instance
        part.config(bd=2, relief=GROOVE)  # or pass configs to Demo()
        part.pack(side=LEFT, expand=YES, fill=BOTH)  # grow, stretch with window
        parts.append(part)  # change list in-place


def dumpState():
    '''
    Dumps state
    '''
    for part in parts:  # run demo report if any
        print(part.__module__ + ':', end=' ')
        if hasattr(part, 'report'):
            part.report()
        else:
            print('none')


root = Tk()  # make explicit root first
root.title('Frames')
Label(root, text='Multiple Frame demo', bg='white').pack()
Button(root, text='States', command=dumpState).pack(fill=X)
Quitter(root).pack(fill=X)
addComponents(root)
root.mainloop()
