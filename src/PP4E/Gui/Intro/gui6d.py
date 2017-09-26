from tkinter import Button
from tkinter import RIGHT
from gui6 import Hello  # @UnresolvedImport


class HelloExtender(Hello):
    '''
    An overriden version of Hello
    '''
    def make_widgets(self):  # extend method here
        '''
        Makes the widgets
        '''
        Hello.make_widgets(self)
        Button(self, text='Extend', command=self.quit).pack(side=RIGHT)

    def message(self):
        '''
        Prints a message
        '''
        print('hello', self.data)  # redefine method here


if __name__ == '__main__':
    HelloExtender().mainloop()
