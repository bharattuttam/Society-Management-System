from tkinter import *
from PIL import Image, ImageTk


class BackGroundPage:
    def __init__(self, root):
        self.root = root
        self.root.iconbitmap('images/societymanagementbackground.jpeg')
        self.root.title('Society Routine Services')
        # ensure that size of image is same as/greater than size of frame
        self.f = Frame(root, width=1600, height=900)
        self.f.pack()

        self.raw_image = Image.open("images/societymanagementbackground.jpeg")
        # define the size of the image, which will also determine the size of the button
        self.raw_image = self.raw_image.resize((1600, 900))
        self.img = ImageTk.PhotoImage(self.raw_image)

        self.panel = Label(self.f, image=self.img)
        self.panel.pack()
        self.panel.pack_propagate(0)
        # Add the message saying "MANOHAR'S CONSTRUCTIONS"
        self.m = Message(self.f, width=600, font=("Monotype Corsiva", 20, "bold", "italic"), text="MANOHAR'S CONSTRUCTIONS",
                         bg="#797ED5", relief=SOLID, borderwidth=2)
        self.m.place(x=120, y=20)
        # The footer at the bottom
        self.footer = Label(self.panel, bg="ivory3", height=1,
                            text="@Copyright 2021 Manohar's Construction pvt. limited All rights reserved")
        self.footer.pack(side=BOTTOM, fill=X)
        self.footer.tkraise()
        self.f.pack_propagate(0)


if (__name__ == "__main__"):
    root = Tk()
    d = BackgroundPage(root)
    root.mainloop()

"""
The file which is executed, uska __name__ ==> "__main__"
All the other file which are not executed, uska __name__ ==> "filename"
"""
