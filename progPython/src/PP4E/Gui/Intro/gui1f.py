from tkinter import mainloop, Label
from tkinter import TOP

widget = Label()
widget['text'] = 'Hello GUI world!'
widget.pack(side=TOP)
mainloop()
