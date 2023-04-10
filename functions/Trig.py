from tkinter import *

class Trig:


    def addButton(self, txt = "Button", bg="gray100", font='arial 12', width=8, height=2):
        btn = Button(self.button_frame, text=txt, font=font, bg=bg, bd=0, width=width, height=height)
        i = len(self.btn_list)
        cur_row = int(i / 3) if i > 0 else 0
        btn.grid(row=cur_row, column=(i % 3), padx=1, pady=1)
        self.btn_list.append(btn)

    def __init__(self, root):

        self.button_frame = Frame(root, bg="gray70", relief='raised', bd=1)
        self.btn_list = []
         
        self.addButton("sinx")
        self.addButton("cosx")
        self.addButton("tanx")

