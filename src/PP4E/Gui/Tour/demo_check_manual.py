"""
check buttons, the hard way (without variables)
"""

from tkinter import Tk, Checkbutton, LEFT
states = []  # change object not name


def onPress(idx):  # keep track of states
    '''
    Press event handler
    :param idx: iteration number
    '''
    states[idx] = not states[idx]  # changes False->True, True->False


root = Tk()
for i in range(10):
    chk = Checkbutton(root, text=str(i), command=(lambda i=i: onPress(i)))
    chk.pack(side=LEFT)
    states.append(False)

root.mainloop()
print(states)  # show all states on exit
