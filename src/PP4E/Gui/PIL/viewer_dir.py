"""
display all images in a directory in pop-up windows
GIFs work in basic tkinter, but JPEGs will be skipped without PIL
"""

import os
import sys
from tkinter import Tk, Toplevel, Label, Button
from PIL.ImageTk import PhotoImage  # <== required for JPEGs and others

IMGDIR = sys.argv[1] if len(sys.argv) > 1 else'images'
imgfiles = os.listdir(IMGDIR)  # does not include directory prefix

main = Tk()
main.title('Viewer')
quitBut = Button(main, text='Quit all', command=main.quit, font=('courier', 25))
quitBut.pack()
savephotos = []

for imgfile in imgfiles:
    imgpath = os.path.join(IMGDIR, imgfile)
    win = Toplevel()
    win.title(imgfile)
    try:
        imgobj = PhotoImage(file=imgpath)
        Label(win, image=imgobj).pack()
        print(imgpath, imgobj.width(), imgobj.height())  # size in pixels
        savephotos.append(imgobj)  # keep a reference
    except:
        errmsg = 'skipping %s\n%s' % (imgfile, sys.exc_info()[1])
        Label(win, text=errmsg).pack()

main.mainloop()
