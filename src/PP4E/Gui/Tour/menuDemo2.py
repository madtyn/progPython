#!/usr/bin/python3
"""
same but add photos in toolbar using PIL to generate images
"""

from tkinter import Frame, Label, Menu, Button,  PhotoImage  # get widget classes
from tkinter import YES, BOTH, SUNKEN, BOTTOM, LEFT, RAISED, RIGHT, DISABLED, X, Y
from tkinter.messagebox import askyesno, showinfo, showerror  # get standard dialogs


class NewMenuDemo(Frame):  # an extended frame
    """
    Menu demo
    """
    def __init__(self, parent=None):  # attach to top-level?
        """
        Constructor
        :param parent: the parent
        """
        # do superclass init
        super().__init__(parent)  # Same as super(__class__, self, parent) and
                                  # Frame.__init__(self, parent) from Python 2.x
        self.pack(expand=YES, fill=BOTH)
        self.createWidgets()  # attach frames/widgets
        self.master.title("Toolbars and Menus")  # set window-manager info
        self.master.iconname("tkpython")  # label when iconified

    def createWidgets(self):
        """
        Builds the widgets
        """
        self.makeMenuBar()
        self.makeToolBar()
        lab = Label(self, text='Menu and Toolbar Demo')
        lab.config(relief=SUNKEN, width=40, height=10, bg='white')
        lab.pack(expand=YES, fill=BOTH)

    # def makeToolBar(self):
    #         """
    #         Builds the toolbar
    #         """
    #    toolbar = Frame(self, cursor='hand2', relief=SUNKEN, bd=2)
    #    toolbar.pack(side=BOTTOM, fill=X)
    #    Button(toolbar, text='Quit',  command=self.quit    ).pack(side=RIGHT)
    #    Button(toolbar, text='Hello', command=self.greeting).pack(side=LEFT)

    def makeToolBar(self, size=(40, 40)):
        """
        Builds the toolbar
        """
        from PIL.ImageTk import PhotoImage, Image  # if jpegs or make new thumbs
        imgdir = r'../PIL/images/'
        toolbar = Frame(self, cursor='hand2', relief=SUNKEN, bd=2)
        toolbar.pack(side=BOTTOM, fill=X)
        photos = 'ora-lp4e-big.jpg', 'PythonPoweredAnim.gif', 'python_conf_ora.gif'
        self.toolPhotoObjs = []
        for file in photos:
            imgobj = Image.open(imgdir + file)  # make new thumb
            imgobj.thumbnail(size, Image.ANTIALIAS)  # best downsize filter
            img = PhotoImage(imgobj)
            btn = Button(toolbar, image=img, command=self.greeting)
            btn.config(bd=2, relief=RAISED)
            btn.config(width=size[0], height=size[1])
            btn.pack(side=LEFT)
            self.toolPhotoObjs.append((img, imgobj))  # keep a reference
        Button(toolbar, text='Quit', command=self.quit).pack(side=RIGHT, fill=Y)

    def makeMenuBar(self):
        """
        Builds the menubar
        """
        self.menubar = Menu(self.master)
        self.master.config(menu=self.menubar)  # master=top-level window
        self.fileMenu()
        self.editMenu()
        self.imageMenu()

    def fileMenu(self):
        """
        Builds the filemenu
        """
        pulldown = Menu(self.menubar)
        pulldown.add_command(label='Open...', command=self.notdone)
        pulldown.add_command(label='Quit', command=self.quit)
        self.menubar.add_cascade(label='File', underline=0, menu=pulldown)

    def editMenu(self):
        """
        Builds the editmenu
        """
        pulldown = Menu(self.menubar)
        pulldown.add_command(label='Paste', command=self.notdone)
        pulldown.add_command(label='Spam', command=self.greeting)
        pulldown.add_separator()
        pulldown.add_command(label='Delete', command=self.greeting)
        pulldown.entryconfig(4, state=DISABLED)
        self.menubar.add_cascade(label='Edit', underline=0, menu=pulldown)

    def imageMenu(self):
        """
        Builds the imagemenu
        """
        photoFiles = ('ora-lp4e.gif', 'pythonPowered.gif', 'python_conf_ora.gif')
        pulldown = Menu(self.menubar)
        self.photoObjs = []
        for file in photoFiles:
            img = PhotoImage(file='../gifs/' + file)
            pulldown.add_command(image=img, command=self.notdone)
            self.photoObjs.append(img)  # keep a reference
        self.menubar.add_cascade(label='Image', underline=0, menu=pulldown)

    def greeting(self):
        """
        Pops up a greeting dialog
        """
        showinfo('greeting', 'Greetings')

    def notdone(self):
        """
        Not done yet handler
        """
        showerror('Not implemented', 'Not yet available')

    def quit(self):
        """
        Quits the application after requesting confirm
        """
        if askyesno('Verify quit', 'Are you sure you want to quit?'):
            Frame.quit(self)


if __name__ == '__main__':
    NewMenuDemo().mainloop()  # if I'm run as a script
