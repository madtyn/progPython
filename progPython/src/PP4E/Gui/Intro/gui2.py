import sys
from tkinter import Button

widget = Button(None, text='Hello widget world', command=sys.exit)
widget.pack()
widget.mainloop()