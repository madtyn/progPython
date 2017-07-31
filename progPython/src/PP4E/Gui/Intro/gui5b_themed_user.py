#!/usr/bin/python3
"""
    Gui example
"""
from tkinter import mainloop, Button
from user_preferences import bcolor, bfont, bsize  # get user settings @UnresolvedImport


class ThemedButton(Button):  # pylint: disable=too-many-ancestors
    '''
    Themed button
    '''
    def __init__(self, parent=None, **configs):
        Button.__init__(self, parent, **configs)
        self.pack()
        self.config(bg=bcolor, font=(bfont, bsize))


def onSpam():
    '''
    Handler for button onSpam
    '''
    print('Spam')


def onEggs():
    '''
    Handler for button onEggs
    '''
    print('Eggs')


ThemedButton(text='spam', command=onSpam)  # normal button widget objects
ThemedButton(text='eggs', command=onEggs)  # all inherit user preferences


class MyButton(ThemedButton):  # subclasses inherit prefs too pylint: disable=too-many-ancestors
    '''
    A custom button
    '''
    def __init__(self, parent=None, **configs):
        ThemedButton.__init__(self, parent, **configs)
        self.config(text='subclass')


MyButton(command=onSpam)
mainloop()
