import tkinter as tk


class ComboBox(tk.Canvas):

    def event_configure(self, e):
        self.delete('base')

        colCout = self.master.grid_size()[0]
        cellWidth = int(self.master.grid_bbox()[3] / colCout)

        x1=0
        x2=x1 + cellWidth
        y1 = 0
        y2 = y1 + e.height

        self.create_rectangle(x1,y1,x2,y2, fill='blue', tags='base')

        print()

    def __init__(self, master=None, width=0, height=0, command=None, *args, **kwargs):
        super(ComboBox, self).__init__(master, *args, **kwargs)
        self.config(bg=self.master["bg"], width=self.master["width"], height=self.master["height"])
        
        self.bg = 'red'
        self.fg = '#ffffff'
        
        self.width = width
        self.height = height

        x = 0
        y = 0

        x1 = x
        x2 = x1 + width

        y1 = y
        y2 = y1 + height
        

        self.create_rectangle(x1,y1,x2,y2, fill='red', tags='base')
        self.bind('<Configure>', self.event_configure)
        