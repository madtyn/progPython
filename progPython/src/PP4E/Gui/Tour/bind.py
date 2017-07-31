"""
    Binding events example
"""
from tkinter import Tk, Label
from tkinter import YES, BOTH


def showPosEvent(event):
    '''
    Shows position of the event input object
    :param event: event
    '''
    print('Widget=%s X=%s Y=%s' % (event.widget, event.x, event.y))


def showAllEvent(event):
    '''
    Show all handler
    :param event: event
    '''
    print(event)
    for attr in dir(event):
        if not attr.startswith('__'):
            print(attr, '=>', getattr(event, attr))


def onKeyPress(event):
    '''
    Key handler
    :param event: event
    '''
    print('Got key press:', event.char)


def onArrowKey(event):
    '''
    Arrow key handler
    :param event: event
    '''
    print('Got up arrow key press')


def onReturnKey(event):
    '''
    Return key handler
    :param event:
    '''
    print('Got return key press')


def onLeftClick(event):
    '''
    Left click key handler
    :param event: event
    '''
    print('Got left mouse button click:', end=' ')
    showPosEvent(event)


def onRightClick(event):
    '''
    Right click key handler
    :param event: event
    '''
    print('Got right mouse button click:', end=' ')
    showPosEvent(event)


def onMiddleClick(event):
    '''
    Middle click key handler
    :param event: event
    '''
    print('Got middle mouse button click:', end=' ')
    showPosEvent(event)
    showAllEvent(event)


def onLeftDrag(event):
    '''
    Left drag handler
    :param event: event
    '''
    print('Got left mouse button drag:', end=' ')
    showPosEvent(event)


def onDoubleLeftClick(event):
    '''
    Double left click handler
    :param event: event
    '''
    print('Got double left mouse click', end=' ')
    showPosEvent(event)
    tkroot.quit()


tkroot = Tk()
labelfont = ('courier', 20, 'bold')  # family, size, style
widget = Label(tkroot, text='Hello bind world')
widget.config(bg='red', font=labelfont)  # red background, large font
widget.config(height=5, width=20)  # initial size: lines,chars
widget.pack(expand=YES, fill=BOTH)

widget.bind('<Button-1>', onLeftClick)  # mouse button clicks
widget.bind('<Button-3>', onRightClick)
widget.bind('<Button-2>', onMiddleClick)  # middle=both on some mice
widget.bind('<Double-1>', onDoubleLeftClick)  # click left twice
widget.bind('<B1-Motion>', onLeftDrag)  # click left and move

widget.bind('<KeyPress>', onKeyPress)  # all keyboard presses
widget.bind('<Up>', onArrowKey)  # arrow button pressed
widget.bind('<Return>', onReturnKey)  # return/enter key pressed
widget.focus()  # or bind keypress to tkroot
tkroot.title('Click Me')
tkroot.mainloop()
