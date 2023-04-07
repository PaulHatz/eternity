from functools import partial
from tkinter import *

from functions.CalcBtn import CalcBtn
from functions.StandardMode import StandardMode

def toggleMenu():
    global showingMenuFrame, menuFrame,buttonFrame
    if showingMenuFrame == True:
        menuFrame.place_forget()
        showingMenuFrame = False
    else:
        menuFrame.place(x=0, y=50)
        menuFrame.focus()
        showingMenuFrame = True

def menuBarFocusOut(e):
    global showingMenuFrame
    menuFrame.place_forget()
    showingMenuFrame = False

def init_menuBar(window):
    global menuFrame, showingMenuFrame
    showingMenuFrame = False
    menuFrame = Frame(window, width=200, height=561, bg="gray80", relief='raised')
    menuFrame.grid_propagate(0)
    menuFrame.bind("<FocusOut>", menuBarFocusOut)


    l=Label(menuFrame, text="CALCULATOR",  font='arial 8', bg="gray80", fg="gray10", anchor=W)
    l.grid(row=0,column=0, pady=5)

    x=Button(menuFrame, text="  Standard", width=22, height=2, bd=0, font='arial 11', bg="gray75", anchor=W)
    x.grid(row=3, column=0)
    
    y=Button(menuFrame, text="  Scientific", width=22, height=2, bd=0, font='arial 11', bg="gray80", anchor=W)
    y.grid(row=4, column=0)
    
    z=Button(menuFrame, text="  Conversion", width=22, height=2, bd=0, font='arial 11', bg="gray80", anchor=W)
    z.grid(row=5, column=0)

def configureWindow(window):
    global previousInput
    previousInput = StringVar()
    #global previousResultField, inputField
    
    stdmode = StandardMode(window)


    headFrame = Frame(window, width=400, height=50, bg="gray100")
    headFrame.pack()
    headFrame.grid_propagate(0)
    
    btn = Button(headFrame, text='☰', height=1, bd=0, bg="gray100", font='arial 12', command=lambda: toggleMenu() )
    btn.grid(row=0,column=0, padx=5)

    title = Label(headFrame, height=2, font=('arial', 16, 'bold'), bg='gray100', text="ETERNITY")
    title.grid(row=0,column=2)

    currentResultField = Label(window, width=45, height=1, font='arial 12', bg='lightblue', textvariable=stdmode.currentInputResult, anchor=E, justify=RIGHT)
    currentResultField.pack(padx=5)
    inputField = Label(window, width=15, height=1, font=('arial', 32, 'bold'), bg='lightblue', textvariable=stdmode.input, anchor=E, justify=RIGHT)
    inputField.pack(padx=5)


    init_menuBar(window)
