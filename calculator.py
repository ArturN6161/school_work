# class Calculator:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#
#     def sum(self):
#         return self.a + self.b
#
#
#     def different(self):
#         return self.a - self.b
#
#
#     def product(self):
#         return self.a * self.b
#
#
#     def quotient(self):
#         return self.a / self.b
#
#
#     def get_info(self, action=""):
#         if action == "+":
#             print(f'numbers: {self.a}, {self.b} is {calc.sum()}')
#         if action == "-":
#             print(f'numbers: {self.a}, {self.b} is {calc.different()}')
#         if action == "*":
#             print(f'numbers: {self.a}, {self.b} is {calc.product()}')
#         if action == "/":
#             print(f'numbers: {self.a}, {self.b} is {calc.quotient()}')
#
#
# calc = Calculator(8, 4)
# calc.get_info("/")


class Python:
    def __init__(self, symbol_input):
        self.symbol_input = symbol_input

    def get_String(self):
        return self.symbol_input


    def print_String(self):
        if self.symbol_input:
          print(self.get_String().upper())


print_symbol = Python(symbol_input="f")
print_symbol.print_String()