"""
Standalone container subclass example
"""
from tkinter import Frame, Label
from tkinter import RIGHT
from gui7c import HelloPackage  # CHANGED: or get from gui7c--__getattr__ added @UnresolvedImport

frm = Frame()
frm.pack()
Label(frm, text='hello').pack()

part = HelloPackage(frm)
part.pack(side=RIGHT)  # FAILS!--need part.top.pack(side=RIGHT)
frm.mainloop()
