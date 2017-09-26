"""
show one image with standard tkinter photo object;
as is this handles GIF files, but not JPEG images; image filename listed in
command line, or default; use a Canvas instead of Label for scrolling, etc.
"""

import os
import sys
from tkinter import Tk, Label, PhotoImage  # use standard tkinter photo object

IMGDIR = 'images'
IMGFILE = sys.argv[1] if len(sys.argv) > 1 else 'london-2010.gif'  # cmdline argument given?
# GIF works, but JPEG requires PIL

IMGPATH = os.path.join(IMGDIR, IMGFILE)

win = Tk()
win.title(IMGFILE)
imgobj = PhotoImage(file=IMGPATH)  # display photo on a Label
Label(win, image=imgobj).pack()
print(imgobj.width(), imgobj.height())  # show size in pixels before destroyed
win.mainloop()
