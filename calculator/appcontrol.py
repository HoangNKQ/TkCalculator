from display import Display
from operation import Operation

class AppControl:
    def __init__(self):
        self.display = Display()
        self.operation = Operation()

    def start_app(self):
        self.display.init_display()



if __name__ == '__main__':
    calculator = AppControl()
    calculator.start_app()