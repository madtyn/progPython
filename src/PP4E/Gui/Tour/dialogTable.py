"""
# define a name:callback demos table
"""

from tkinter.colorchooser import askcolor  # they live in Lib\tkinter
from tkinter.simpledialog import askfloat
from tkinter.filedialog import askopenfilename  # get standard dialogs
from tkinter.messagebox import askquestion, showerror


demos = {
    'Open': askopenfilename,
    'Color': askcolor,
    'Query': lambda: askquestion('Warning', 'You typed "rm *"\nConfirm?'),
    'Error': lambda: showerror('Error!', "He's dead, Jim"),
    'Input': lambda: askfloat('Entry', 'Enter credit card number')
}
