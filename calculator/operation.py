import math

class Operation:
    def __init__(self):
        self.result = 0

    def str_to_num(self, str):
        num = 0
        if '.' in str:
            num = float(str)
        else:
            num = int(str)

    def evaluate(self, equation_string: str):
        if '+' in equation_string:
            number = equation_string.split('+')
            self. result = self.str_to_num(number[0]) + self.str_to_num(number[1])

        if '-' in equation_string:
            number = number = equation_string.split('-')
            self. result = self.str_to_num(number[0]) - self.str_to_num(number[1])

        if 'x' in equation_string:
            number = number = equation_string.split('x')
            self. result = self.str_to_num(number[0]) * self.str_to_num(number[1])

        if '÷' in equation_string:
            number = number = equation_string.split('÷')
            self. result = self.str_to_num(number[0]) / self.str_to_num(number[1])

        return self.result