import tkinter as tk
from tkinter import ttk

class Display(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title ('Calculator')
        self.setup_frame()
        self.init_frame()
        
    def setup_frame(self):
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 6)
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)

    def init_frame(self):
        expression = self.create_expression_frame(self)
        expression.grid(row= 0, column = 0, sticky= 'nsew')

    def create_expression_frame(self, parent):
        expression_frame = ttk.Frame(parent)
        expression_frame.rowconfigure(0, weight = 1)
        expression_frame.rowconfigure(1, weight = 4)
        expression_frame.columnconfigure(0, weight = 1)

        equation_label = ttk.Label(expression_frame, text= "equation")
        equation_label.grid(row= 0, column= 0, sticky= 'e')

        result_label = ttk.Label(expression_frame, text= "Result", font=('Arial', 30))
        result_label.grid(row= 1, column= 0, sticky = 'e')

        return expression_frame

    def init_display(self):
        self.mainloop()