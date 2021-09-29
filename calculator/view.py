import tkinter as tk
from tkinter import ttk
from tkinter import font

class View(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.title ('Calculator')
        self.resizable(False, False)
        self.geometry('500x600')
        # self.tk.call("source", "theme\sun-valley.tcl")
        # self.tk.call("set_theme", "dark")

        self.main_entry = ''
        self.expression = ''

        self.setup_frame()
        self.init_frame()
        

    def setup_frame(self):
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 6)
        self.columnconfigure(0, weight = 1)
        #self.columnconfigure(1, weight = 1)


    def init_frame(self):
        expression = self.create_expression_frame(self)
        expression.grid(row= 0, column = 0, sticky= 'nsew', padx= 5, pady= 5)
        button = self.create_button_frame(self)
        button.grid(row= 1, column = 0, sticky= 'nsew')


    def create_expression_frame(self, parent):
        expression_frame = ttk.Frame(parent)
        expression_frame.rowconfigure(0, weight = 1)
        expression_frame.rowconfigure(1, weight = 3)
        expression_frame.columnconfigure(0, weight = 1)

        self.expression_label = ttk.Label(expression_frame, text= '', font=('Arial', 10))
        self.expression_label.grid(row= 0, column= 0, sticky= 'e', padx= 5, pady= 5)

        self.main_label = ttk.Label(expression_frame, text= "0", font=('Arial', 35))
        self.main_label.grid(row= 1, column= 0, sticky = 'e', padx= 5, pady= 5)

        return expression_frame

    def get_main_text(self):
        return self.main_label['text']

    def insert_expression(self, expression_text):
        self.expression_label.configure(text= expression_text)

    def insert_main_entry(self, main_text):
        self.main_label.configure(text= main_text)


    def create_button_frame(self, parent):
        # Variables
        # buttons = [
        #     '(',')','C','+',
        #     '7','8','9','-',
        #     '4','5','6','*',
        #     '1','2','3','/',
        #     '+/-','0','.','='
        #     ]

        self.buttons = {
            'pi':'\u03C0', 'percentage':'%', 'Clear':'C', 'erase_left':'\u232b',
            'sqr':'x\u00b2' , 'root2':'\u221a', '1/x':'1/x', '+':'+',
            '7':'7', '8':'8', '9':'9', '-':'-',
            '4':'4', '5':'5', '6':'6', '*':'\u00D7',
            '1':'1', '2':'2', '3':'3', '/':'\u00F7',
            '+/-':'+/-', '0':'0', '.':'.', '=':'='
        }
        rows = 6
        r = 0
        c = 0

        # Button Frame
        button_frame = ttk.Frame(parent) 
        s = ttk.Style()
        s.configure('TButton', font=('Arial', 16))

        # Grid management
        for i in range(rows):
            if i < 4:
                button_frame.columnconfigure(i, weight = 1)
            button_frame.rowconfigure(i, weight = 1)
        
        # Create Button
        # for i in range(len(buttons)):
        #     button = ttk.Button(
        #         button_frame, 
        #         style= 'TButton',
        #         text= buttons[i], 
        #         command= (lambda txt = buttons[i]: self.controller.button_trigger(txt))
        #     )
        #     button.grid(row= r, column= c, sticky='nsew', padx= 2, pady= 2)
        #     c = c + 1 
        #     if c == 4:
        #         c = 0
        #         r = r + 1

        for name, symbol in self.buttons.items():
            button = ttk.Button(
                button_frame, 
                style= 'TButton',
                text= symbol, 
                command= (lambda txt = name: self.controller.button_trigger(txt))
            )
            button.grid(row= r, column= c, sticky='nsew')
            c = c + 1 
            if c == 4:
                c = 0
                r = r + 1

        return button_frame


    def init_display(self):
        self.mainloop()


def main():
    pass

if __name__ == '__main__':
    main()