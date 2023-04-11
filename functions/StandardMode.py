from functools import partial

from tkinter import *

#from functions.ComboBox import *
#from functions.Trig import *

from functions.formulas import *


def fact(n):
    return factorial(int(n))



class StandardMode:

    def performCalc(self, calc):
        op_dict = { '×': '*', '÷': '/', '^': '**', '√': "sqrt" }
        final_calc = calc
        for op, alias in op_dict.items():
            final_calc = final_calc.replace(op, alias)

        func_dict = { 'log': calc_log, 'ln': ln, 'sqrt': calc_sqrt, 'gamma': gamma, 'sinh': sinh, 'sin': sint, 'cos': cost, 'tan': tant }
        return eval(final_calc, func_dict)

    def getCurInputFiltered(self):
        cur_input = self.input.get()
        if len(cur_input) > 0 and cur_input[0] == "-":
            new_cur_input = "(" + cur_input + ")"
        else:
            new_cur_input = cur_input

        return new_cur_input
    
    def opBtn(self, text):
        basic_math_operators = ['+', '-', '÷', '×', '^']

        cur_input = self.input.get()

        if self.resetInput == True:
            if len(self.cur_input_list) == 0 and len(cur_input) > 0:
                self.resetInput = False

        if len(self.cur_input_list) > 0 and self.cur_input_list[-1] in basic_math_operators:
            if len(cur_input) == 0:
                return
           
        if self.is_preview_res == False:
            self.insert_to_curinput(self.getCurInputFiltered())
            if self.lParCount == 0:
                self.input.set(self.performCalc(self.currentInputResult.get()))

        self.insert_to_curinput(text)
        self.resetInput = True
        self.is_preview_res = False

    def eqBtn(self):
        if len(self.cur_input_list) > 0 and self.cur_input_list[-1] != "=":           
            if self.is_preview_res == False:
                self.insert_to_curinput(self.getCurInputFiltered())

            if self.lParCount == 0:
                ans = self.performCalc(self.currentInputResult.get())
                self.f = open("history" + ".txt", 'a')
                self.f.write(self.currentInputResult.get() + "=" + str(ans) + "\n")
                self.f.close()
                self.input.set(ans)
                self.insert_to_curinput('=')
                self.is_preview_res = False
                self.resetInput = True

    def eq_par(self, idx):
        l = [i for i, n in enumerate(self.cur_input_list) if n == '(']
        r = [i for i, n in enumerate(self.cur_input_list) if n == ')']


        n = -idx #nth from end.

        if idx == 0:
            ct = 0
            j = len(self.cur_input_list) - 1
            for item in self.cur_input_list[::-1]:
                if item == ")":
                    ct += 1
                elif item == "(":
                    ct -= 1
                if ct == 0:
                    break
                j -= 1
        
        i = j if idx == 0 else l[n]
       
        s = str(''.join(self.cur_input_list[i:]))
        return self.performCalc(s)

    def parBtn(self, txt):
        if txt == "(":
            self.lParCount += 1
            self.insert_to_curinput(txt)

        elif txt == ")":
            if self.lParCount <= 0:
                return
            
            if self.lParCount > 0:
                self.lParCount -= 1
                if self.is_preview_res == False:
                    self.insert_to_curinput(self.getCurInputFiltered())
                self.insert_to_curinput(txt)
                self.input.set(self.eq_par(self.lParCount))
                self.is_preview_res = True
    
    def btn_factorial(self):
        cur_input = self.input.get()
        self.insert_to_curinput("fact(" + cur_input + ")")
        self.input.set(fact(cur_input))
        self.resetInput = True
        self.is_preview_res = True
    
    
    def btn_sqrt(self):
        X = float(self.input.get())
        self.input.set(self.calc_sqrt(X))
        self.insert_to_curinput(str("√(" + str(X) + ")"))
        self.is_preview_res = True
        self.resetInput = True

    def btn_log(self, B=10):
        X = float(self.input.get())
        self.input.set(calc_log(B, X))
        self.insert_to_curinput(str("log(" + str(B) + ", " + str(X) + ")"))
        self.is_preview_res = True
        self.resetInput = True        


    def btn_sinh(self):
        x = float(self.input.get())
        self.input.set(sinh(x))
        self.insert_to_curinput("sinh(" + str(x) + ")")
        self.is_preview_res = True
        self.resetInput = True

    def btn_clearInput(self):
        self.input.set("0")
        self.lParCount = 0

    def btn_store(self):
        self.storedValues.append(float(self.input.get()))
        self.resetInput = True

    def btn_erase(self):
        self.storedValues = []

    def btn_stddev(self):
        m = sum(self.storedValues)/len(self.storedValues)
        var = sum(pow(x - m,2) for x in self.storedValues)/(len(self.storedValues)-1)
        stddev = var **0.5
        print(stddev)
        self.input.set(stddev)
        self.resetInput = True
        self.is_preview_res = True

    def btn_gamma(self):
        result = gamma(int(self.input.get()))
        self.insert_to_curinput("gamma(" + self.input.get() + ")")
        self.input.set(result)
        self.is_preview_res = True
        self.resetInput = True

    def btn_MAD(self):
        median_vals = sum(self.storedValues) / len(self.storedValues)

        dev = 0

        for x in self.storedValues:
            dev += abs(x - median_vals)

        self.input.set(dev/len(self.storedValues))
        self.resetInput = True

    def handleButton(self, text, action = None):
        cur_input = self.input.get()
        basic_math_operators = ['+', '-', '÷', '×', '^']

        if self.resetInput == True and len(self.cur_input_list) > 0 and self.cur_input_list[-1] == "=":
            self.clear_input_list()
            #self.resetInput = False

        if action == None:
            if text.isnumeric():
                if self.resetInput == True:
                    cur_input = ""
                    self.resetInput = False
                if len(cur_input) > 0 and len(cur_input) <= 2:
                    if cur_input[-1] != '.' and ((cur_input[0] == '-' and cur_input[1] == '0') or (cur_input[0] == '0')):
                        cur_input = cur_input[:-1]
                
                self.input.set(cur_input + text)
            
            elif text in basic_math_operators:
                self.opBtn(text)

        else:         
            action()

    def toggleNegative(self):
        if len(self.input.get()) > 0 and self.input.get()[0] == "-":
            self.input.set(self.input.get()[1:])
        else:
            self.input.set("-" + (self.input.get() if len(self.input.get()) > 0 else "0"))

    def insertDecimal(self):
        cur_input = self.input.get()

        if self.resetInput == True:
            cur_input = "0"
            self.resetInput = False
            self.op_lock = False

        if cur_input.find(".") == -1:
            self.input.set(cur_input + ".")

    def backspace(self):
        cur_input = self.input.get()

        if len(cur_input) >= 1:
            first_digit_loc = 0 if cur_input[0] != '-' else 1
            
            digits = cur_input[first_digit_loc:]
            if len(digits) > 1:
                self.input.set(cur_input[:-1])
            else:
                self.input.set("0")

    def addButton(self, txt = "Button", alias=None, action = None, bg="gray94", font='arial 12', width=10, height=2):
        btn = Button(self.buttonFrame, text=txt, command=lambda: self.handleButton(txt if alias == None else alias, action), font=font, bg=bg, bd=0, width=width, height=height)
        i = len(self.btn_list)
        cur_row = int(i / 4) if i > 0 else 0
        btn.grid(row=cur_row, column=(i % 4), padx=1, pady=1)
        self.btn_list.append(btn)


    def updateCurrentinputResult(self):
        text = ""
        for x in self.cur_input_list:
            text = text + x + " "
        
        self.currentInputResult.set(text)

    def insert_to_curinput(self, str):
        self.cur_input_list.append(str)
        self.updateCurrentinputResult()

    def remove_last_curinput(self):
        self.cur_input_list = self.cur_input_list[:-1]
        self.updateCurrentinputResult()

    def clear_input_list(self):
        self.cur_input_list = []
        self.updateCurrentinputResult()

    def clear(self):
        self.cur_input_list = []
        self.updateCurrentinputResult()
        self.input.set("0")
        self.is_preview_res = False
        self.resetInput = False
        self.lParCount = 0


    def test_btn(self):
        self.log_base = int(self.input.get())
        self.resetInput = True
        
    def test_btn2(self):
        self.input.set(calc_log(B=self.log_base, X=self.input.get()))
        self.resetInput = True 

    def btn_sinx(self):
        x = float(self.input.get())

        self.insert_to_curinput("sin(" + str(x) + ")")
        self.input.set(sint(x))
        
        self.resetInput = True
        self.is_preview_res = True

    def btn_cosx(self):
        x = float(self.input.get())

        self.insert_to_curinput("cos(" + str(x) + ")")
        self.input.set(self.cost(x))
        
        self.resetInput = True
        self.is_preview_res = True

    def btn_tanx(self):
        x = float(self.input.get())

        self.insert_to_curinput("tan(" + str(x) + ")")
        self.input.set(self.tant(x))
        
        self.resetInput = True
        self.is_preview_res = True


    #Weight Units

    def __init__(self, window):
        self.node_list = []

        self.window = window
        self.btn_list = []


        self.buttonFrame = Frame(window, bg='gray90')
        self.buttonFrame.pack(side=BOTTOM)
        self.input = StringVar(value="0")
        self.currentInputResult = StringVar()
        self.cur_input_list = []

        self.resetInput = False
        self.is_preview_res = False
        self.lParCount = 0
        self.storedValues = []
        self.log_base = 10
        self.angle_mode = "rad"

        self.addButton("2nd")
        self.addButton("CE", action=lambda: self.btn_clearInput())
        self.addButton("C", action=lambda: self.clear())
        self.addButton("←", action=lambda: self.backspace())

        self.addButton("log", action=lambda: self.btn_log())
        self.addButton("xʸ", alias="^")
        self.addButton("√", action=lambda: self.btn_sqrt())
        self.addButton("𝑛!", action=lambda: self.btn_factorial())

        self.addButton("ln")
        self.addButton("(", action=lambda: self.parBtn("("))
        self.addButton(")",  action=lambda: self.parBtn(")"))
        self.addButton("÷")

        self.addButton("7", bg="gray100")
        self.addButton("8", bg="gray100")
        self.addButton("9", bg="gray100")
        self.addButton('×')

        self.addButton("4", bg="gray100")
        self.addButton("5", bg="gray100")
        self.addButton("6", bg="gray100")
        self.addButton("-")
        
        self.addButton("1", bg="gray100")
        self.addButton("2", bg="gray100")
        self.addButton("3", bg="gray100")
        self.addButton("+")

        self.addButton("+/-", bg="gray100", action=lambda: self.toggleNegative())
        self.addButton("0", bg="gray100")
        self.addButton(".", bg="gray100", action=lambda: self.insertDecimal())
        self.addButton("=", bg="lightblue", action=lambda: self.eqBtn())

        self.addButton("STORE", action=lambda: self.btn_store())
        self.addButton("ERASE", action=lambda: self.btn_erase())
        self.addButton("STD", action=lambda: self.btn_stddev())
        self.addButton("log(b,x)", action=lambda: self.test_btn2())

        self.addButton("B", action=lambda: self.test_btn())
        self.addButton("Γ(x)", action=lambda: self.btn_gamma())
        self.addButton("MAD", action=lambda: self.btn_MAD())
        self.addButton("sinh", action=lambda: self.btn_sinh())

        self.addButton("sinx", action=lambda: self.btn_sinx())
        self.addButton("cosx", action=lambda: self.btn_cosx())
        self.addButton("tanx", action=lambda: self.btn_tanx())