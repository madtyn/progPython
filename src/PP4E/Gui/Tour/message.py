"""
    Message widget example
"""
from tkinter import mainloop, Message, X, YES


msg = Message(text="Oh by the way, which one's Pink?")
msg.config(bg='pink', font=('times', 16, 'italic'))
msg.pack(fill=X, expand=YES)
mainloop()
