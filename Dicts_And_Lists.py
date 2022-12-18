from Operators import *

"""
this file contains all of the helpful lists that other files use
"""

# a dictionary of the orders of each operator
OPERATORS_ORDER = {'+': Add.ORDER, '-': Sub.ORDER, '*': Mul.ORDER,
                   '/': Div.ORDER, '^': Pow.ORDER, '%': Modulo.ORDER,
                   '$': Max.ORDER, '&': Min.ORDER, '@': Avg.ORDER, '~': Not.ORDER,
                   '!': Assembly.ORDER, '#': AddDigits.ORDER}

# a dictionary with the function of each operator
# will be called by putting () after
OPERATORS_FUNCS = {'+': Add.calculate_2_operands, '-': Sub.calculate_2_operands, '*': Mul.calculate_2_operands,
                   '/': Div.calculate_2_operands, '^': Pow.calculate_2_operands, '%': Modulo.calculate_2_operands,
                   '$': Max.calculate_2_operands, '&': Min.calculate_2_operands, '@': Avg.calculate_2_operands,
                   '~': Not.calculate_1_operand, '!': Assembly.calculate_1_operand, '#': AddDigits.calculate_1_operand}

# a list of all the possible operators
OPERATORS_LIST = ['+', '-', '*', '/', '^', '%', '$', '&', '@', '~', '!', '#']

# a list of the operators that take only 1 operand
OPERATOR_FOR_1_OPERAND = ['~', '!', '#']

