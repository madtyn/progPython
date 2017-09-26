"""
use StringVar variables
lay out by columns: this might not align horizontally everywhere (see entry2)
"""

from tkinter import Tk, Frame, Label, Entry, StringVar, Button
from tkinter import X, TOP, YES, LEFT, RIGHT
from quitter import Quitter
FIELDS = 'Name', 'Job', 'Pay'


def fetch(variables):
    '''
    Prints the entries' variables
    :param variables: the variables
    '''
    for variable in variables:
        print('Input => "%s"' % variable.get())  # get from var


def makeform(parent, fields):
    '''
    Builds the form
    :param root: the parent
    :param fields: the fields
    '''
    form = Frame(parent)  # make outer frame
    left = Frame(form)  # make two columns
    rite = Frame(form)
    form.pack(fill=X)
    left.pack(side=LEFT)
    rite.pack(side=RIGHT, expand=YES, fill=X)  # grow horizontal

    variables = []
    for field in fields:
        lab = Label(left, width=5, text=field)  # add to columns
        lab.pack(side=TOP)

        var = StringVar()
        ent = Entry(rite)
        ent.pack(side=TOP, fill=X)  # grow horizontal
        ent.config(textvariable=var)  # link field to var
        var.set('enter here')
        variables.append(var)
    return variables


if __name__ == '__main__':
    root = Tk()
    vars_ = makeform(root, FIELDS)
    Button(root, text='Fetch', command=(lambda: fetch(vars_))).pack(side=LEFT)
    Quitter(root).pack(side=RIGHT)
    root.bind('<Return>', (lambda __: fetch(vars_)))
    root.mainloop()
