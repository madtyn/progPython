"""
show one image with PIL photo replacement object
handles many more image types; install PIL first: placed in Lib\site-packages
"""

import os
import sys
from tkinter import Tk, Label
# from PIL.ImageTk import PhotoImage  # <== use PIL replacement class
from PIL.ImageTk import PhotoImage
                                         # rest of code unchanged
IMGDIR = 'images'
IMGFILE = sys.argv[1] if len(sys.argv) > 1 else 'florida-2009-1.jpg'  # does gif, jpg, png, tiff, etc.

IMGPATH = os.path.join(IMGDIR, IMGFILE)

win = Tk()
win.title(IMGFILE)
imgobj = PhotoImage(file=IMGPATH)  # now JPEGs work!
Label(win, image=imgobj).pack()
win.mainloop()
print(imgobj.width(), imgobj.height())  # show size in pixels on exit
