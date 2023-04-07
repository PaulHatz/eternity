from functools import partial
from tkinter import *
from tkinter import messagebox
import os

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

def viewHistoryBtn():
    os.startfile("history.txt")

def sendHistoryBtn():
    if os.path.exists("history.txt"):
        f = open("history.txt")
        os.startfile('mailto://&subject="History"&body=' + f.read())


def clearHistoryBtn():
    if os.path.exists("history.txt"):
        os.remove("history.txt")
        messagebox.showinfo("Success!", "History deleted.")
    else:
        messagebox.showinfo("Success!", "")


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
    
    
    
    l2= Label(menuFrame, text= "CONVERTER", font='arial 8', bg='gray80', fg='gray10', anchor=W)
    l2.grid(row=4, column=0, pady=5)

    lengthBtn=Button(menuFrame, text="  Length", command=lambda: sendHistoryBtn(), width=22, height=2, bd=0, font='arial 11', bg="gray80", anchor=W)
    lengthBtn.grid(row=5, column=0)
    
    volumeBtn=Button(menuFrame, text="  Volume", command=lambda: sendHistoryBtn(), width=22, height=2, bd=0, font='arial 11', bg="gray80", anchor=W)
    volumeBtn.grid(row=6, column=0)

    weightBtn=Button(menuFrame, text="  Weight", command=lambda: sendHistoryBtn(), width=22, height=2, bd=0, font='arial 11', bg="gray80", anchor=W)
    weightBtn.grid(row=7, column=0)

    timeBtn=Button(menuFrame, text="  Time", command=lambda: sendHistoryBtn(), width=22, height=2, bd=0, font='arial 11', bg="gray80", anchor=W)
    timeBtn.grid(row=8, column=0)


    l3= Label(menuFrame, text= "HISTORY", font='arial 8', bg='gray80', fg='gray10', anchor=W)
    l3.grid(row=9, column=0, pady=5)


    y=Button(menuFrame, text="  View History", command=lambda: viewHistoryBtn(), width=22, height=2, bd=0, font='arial 11', bg="gray80", anchor=W)
    y.grid(row=10, column=0)

    z=Button(menuFrame, text="  Clear History", command=lambda: clearHistoryBtn(), width=22, height=2, bd=0, font='arial 11', bg="gray80", anchor=W)
    z.grid(row=11, column=0)


def bind_KeyPress(e, stdmode):
    c = e.char

    if c.isnumeric():
        stdmode.handleButton(c)
    else:
        if c ==  '*':
            stdmode.handleButton('×')
        elif c ==  '/':
            stdmode.handleButton('÷')
        elif c ==  '+':
            stdmode.handleButton('+')
        elif c ==  '-':
            stdmode.handleButton('-')
        elif c ==  '.':
            stdmode.insertDecimal()
        elif c ==  '(':
            stdmode.parBtn("(")
        elif c ==  ')':
            stdmode.parBtn(")")
        elif c ==  '^':
            stdmode.handleButton('^')
        elif c ==  '!':
            stdmode.btn_factorial()
        elif c ==  '\b':
            stdmode.backspace()
        elif c ==  '=':
            stdmode.eqBtn()

def configureWindow(window, old_root):
    global previousInput
    previousInput = StringVar()
    #global previousResultField, inputField
    

    stdmode = StandardMode(window)
    old_root.bind('<KeyPress>', lambda e: bind_KeyPress(e, stdmode))

    headFrame = Frame(window, width=450, height=50, bg="gray100")
    headFrame.pack()
    headFrame.grid_propagate(0)
    
    btn = Button(headFrame, text='☰', height=1, bd=0, bg="gray100", font='arial 12', command=lambda: toggleMenu() )
    btn.grid(row=0,column=0, padx=5)

    title = Label(headFrame, height=2, font=('arial', 16, 'bold'), bg='gray100', text="ETERNITY")
    title.grid(row=0,column=2)

    currentResultField = Label(window, width=50, height=1, font='arial 12', bg='lightblue', textvariable=stdmode.currentInputResult, anchor=E, justify=RIGHT)
    currentResultField.pack(padx=5)
    inputField = Label(window, width=50, height=1, font=('arial', 32, 'bold'), bg='lightblue', textvariable=stdmode.input, anchor=E, justify=RIGHT)
    inputField.pack(padx=5)


    init_menuBar(window)
