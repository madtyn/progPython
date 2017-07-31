from tkinter import Button, Tk, mainloop
from PIL import Image, ImageTk

imgdir = '.\\'
main = Tk()

imageobj = Image.open(imgdir + "ora-lp4e.jpg")
photoimg = ImageTk.PhotoImage(imageobj)
Button(image=photoimg).pack()


mainloop()
