# class Calculator:

def summma(a, b):
    return a + b


def different(a, b):
    return a - b


def product(a, b):
    return a * b


def quotient(a, b):
    if b != 0:
        return a / b
    else:
        raise ZeroDivisionError


# def get_info(action=""):
#     if action == "+":
#         print(f'numbers: {a}, {b} is {calc.sum()}')
#     if action == "-":
#         print(f'numbers: {a}, {b} is {calc.different()}')
#     if action == "*":
#         print(f'numbers: {a}, {b} is {calc.product()}')
#     if action == "/":
#         print(f'numbers: {a}, {b} is {calc.quotient()}')


summma(8, 4)
different(8, 4)
product(8, 4)
#quotient(8, 0)
quotient(8, 4)

# class Python:
# #     def __init__(, symbol_input = None):
# #         symbol_input = symbol_input
# #
# #     def get_String():
# #         symbol_input = input('Введите текст, чтобы вернуть его в верхнем регистре: ')
# #
# #     def print_String():
# #         print(f'Вот текст в верхнер регистре: {symbol_input.upper()}')
# #
# #
# # print_symbol = Python()
# # print_symbol.get_String()
# # print_symbol.print_String()


