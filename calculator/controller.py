
from view import View
from model import Model

class Controller:
    def __init__(self):
        self.view = View(self)
        self.model = Model()


    def start_app(self):
        '''
        Khoi dong app tu Controller 
        '''
        self.view.init_display()


    def update_expression(self):
        '''
        Cap nhat hien thi cong thuc trong view.expression
        '''
        self.view.expression = self.model.expression_text
        self.view.insert_expression(self.view.expression)


    def button_trigger(self, button_name):
        '''
        Xu ly cac chuc nang cua nut bam
        '''    
        if button_name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
            self.view.main_entry = self.model.store_input(button_name, self.view.buttons[button_name])
            self.view.insert_main_entry(self.view.main_entry)
            self.update_expression()


        if button_name == '+':
            self.view.main_entry = self.model.operator('addition', self.view.buttons[button_name])
            self.view.insert_main_entry(self.view.main_entry)
            self.update_expression()


        if button_name == '-':
            self.view.main_entry = self.model.operator('substraction', self.view.buttons[button_name])
            self.view.insert_main_entry(self.view.main_entry)
            self.update_expression()


        if button_name == '*':
            self.view.main_entry = self.model.operator('multiplication', self.view.buttons[button_name])
            self.view.insert_main_entry(self.view.main_entry)
            self.update_expression()


        if button_name == '/':
            self.view.main_entry = self.model.operator('division', self.view.buttons[button_name])
            self.view.insert_main_entry(self.view.main_entry)
            self.update_expression()


        if button_name == 'erase_left':
            pass


        if button_name == '=':
            self.view.main_entry = self.model.equal()
            self.view.insert_main_entry(self.view.main_entry)


        if button_name == '+/-':
            self.view.main_entry = self.model.inverse()
            self.view.insert_main_entry(self.view.main_entry)
            self.update_expression()


        if button_name == 'sqr':
            self.view.main_entry = self.model.square()
            self.view.insert_main_entry(self.view.main_entry)
            self.update_expression()


        if button_name == 'root2':
            self.view.main_entry = self.model.square_root(self.view.buttons[button_name])
            self.view.insert_main_entry(self.view.main_entry)
            self.update_expression()


        if button_name == '1/x':
            self.view.main_entry = self.model.fraction()
            self.view.insert_main_entry(self.view.main_entry)
            self.update_expression()


        if button_name == 'percentage':
            self.view.main_entry = self.model.percentage()
            self.view.insert_main_entry(self.view.main_entry)
            self.update_expression()


        if button_name == 'pi':
            self.view.main_entry = self.model.pi_number(self.view.buttons[button_name])
            self.view.insert_main_entry(self.view.main_entry)
            self.update_expression()


        if button_name == 'Clear':
            self.model.clear()
            self.view.main_entry = self.model.new_value_text
            self.view.main_label['text'] = self.view.main_entry
            self.view.expression = self.model.expression_text
            self.view.expression_label['text'] = self.view.expression
        

def main():
    controller = Controller()
    controller.start_app() 


if __name__ == '__main__':
    main()