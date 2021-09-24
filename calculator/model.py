import math
from tkinter.constants import TRUE


class Model:
    def __init__(self):
        self.two_operand = False
        self.result_value = 0
        self.new_value = 0
        self.new_value_text = ''
        self.operator_name = ''
        self.expression_text = ''
        self.new_expression = True


    def store_input(self, input_button, input_symbol):
        '''
        Luu gia tri so va dau cham vao bien self.current_value
        Chi cho phep mot dau cham trong gia tri duoc nhap vao
        '''
        if input_button == '.' or input_symbol == '.':
            if '.' in self.new_value_text:
                return
        self.new_value_text += input_button
        self.store_expression(input_button)
        self.new_expression = False
        self.new_value = float(self.new_value_text)

        return self.new_value_text 


    def store_expression(self, text):
        if self.new_expression:
            self.expression_text = ''
            self.expression_text += text
            self.new_expression = False
        else:
            self.expression_text += text


    def equal(self):
        self.new_value_text = ''
        if self.two_operand == False:
            self.result_value = self.new_value
        else:
            self.result_value = self.calculate_result_value()
            self.two_operand = False

        self.new_expression = True
        self.new_value = self.result_value

        return self.result_value


    def operator(self, operator_name, operator_symbol):
        self.new_value_text = ''
        # print (self.current_value)
        if self.two_operand == False:
            self.result_value = self.new_value
            self.expression_text = ''
            self.store_expression(str(self.result_value) + operator_symbol)
            self.two_operand = True
        else:
            self.result_value = self.calculate_result_value()
            self.expression_text = ''
            self.store_expression(str(self.result_value) + operator_symbol)

        self.operator_name = operator_name
        self.new_value = self.result_value
        
        return self.result_value


    def calculate_result_value(self):
        if self.operator_name == 'addition':
            self.result_value += self.new_value

        if self.operator_name == 'substraction':
            self.result_value -= self.new_value

        if self.operator_name == 'multiplication':
            self.result_value *= self.new_value

        if self.operator_name == 'division':
            self.result_value /= self.new_value

        return self.result_value


    def inverse(self):
        self.new_value_text = ''
        self.two_operand = False
        self.new_value = -1 * self.new_value
        self.new_expression = True
        self.store_expression(str(self.new_value))
        return self.new_value

    def pi_number(self, symbol):
        self.new_value_text = ''
        self.two_operand = False
        self.new_value = math.pi
        self.new_expression = True
        self.store_expression(symbol)
        return self.new_value

    def square(self):
        self.new_value_text = ''
        self.two_operand = False
        self.new_value = self.new_value**2
        self.new_expression = True
        self.store_expression(str(self.new_value))
        return self.new_value

    def square_root(self, symbol):
        self.new_value_text = ''
        self.two_operand = False
        self.new_value = math.sqrt(self.new_value)
        self.new_expression = True
        self.store_expression(symbol + str(self.new_value))
        return self.new_value

    def fraction(self):
        self.new_value_text = ''
        self.two_operand = False
        self.new_value = 1 / self.new_value
        self.new_expression = True
        self.store_expression(str(self.new_value))
        return self.new_value

    def percentage(self):
        self.new_value_text = ''
        self.two_operand = False
        self.new_value = self.new_value / 100
        self.new_expression = True
        self.store_expression(str(self.new_value))
        return self.new_value

    def clear(self):
        self.two_operand = False
        self.new_expression = True
        self.result_value = 0
        self.new_value = 0
        self.new_value_text = ''
        self.expression_text = ''



def main():
    pass

if __name__ == '__main__':
    main()