"""
radio buttons, the hard way (without variables)
note that deselect for radio buttons simply sets the button's
associated value to a null string, so we either need to still
give buttons unique values, or use checkbuttons here instead;
"""
from tkinter import Tk, Radiobutton, LEFT

state = ''
buttons = []


def onPress(idx):
    '''
    Press handler
    :param idx: the iteration number
    '''
    global state
    state = idx
    for btn in buttons:
        btn.deselect()
    buttons[idx].select()


root = Tk()
for i in range(10):
    rad = Radiobutton(root, text=str(i),
                      value=str(i), command=(lambda i=i: onPress(i)))
    rad.pack(side=LEFT)
    buttons.append(rad)


onPress(0)  # select first initially
root.mainloop()
print(state)  # show state on exit
