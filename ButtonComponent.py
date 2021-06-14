from tkinter import *

class GrayButton(Button):
    def __init__(self,parent,text,command,**kwargs):
        super().__init__(parent, text=text, width=20,height=2, activebackground="#FDF509",activeforeground="#3B80D0",command=command)
        self.configure(**kwargs)

class WhiteButton(Button):
    def __init__(self,parent,text,command,**kwargs):
        super().__init__(parent, text=text, width=25, height=2, bg="blue", fg="#FDF509", activebackground="gray",command=command)
        self.configure(**kwargs)