from tkinter import Tk, Button
from tkinter import LEFT, BOTH, YES

root = Tk()
Button(root, text='press', command=root.quit).pack(side=LEFT, expand=YES, fill=BOTH)
root.mainloop()