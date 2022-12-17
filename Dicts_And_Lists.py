from Operators import *
"""
this file contains all of the helpful lists that other files use
"""

# a dictionary of the orders of each operator
OPERATORS_ORDER = {'+': Add.ORDER, '-': Sub.ORDER, '*': Mul.ORDER,
                   '/': Div.ORDER, '^': Pow.ORDER, '%': Modulu.ORDER,
                   '$': Max.ORDER, '&': Min.ORDER, '@': Avg.ORDER, '~': Not.ORDER,
                   '!': Assembly.ORDER, '#': AddDigits.ORDER}

# a dictionary with the function of each operator
# will be called by putting () after
OPERATORS_FUNCS = {'+': Add.Calculate_2_Operands, '-': Sub.Calculate_2_Operands, '*': Mul.Calculate_2_Operands,
                   '/': Div.Calculate_2_Operands, '^': Pow.Calculate_2_Operands, '%': Modulu.Calculate_2_Operands,
                   '$': Max.Calculate_2_Operands, '&': Min.Calculate_2_Operands, '@': Avg.Calculate_2_Operands,
                   '~': Not.Calculate_1_Operand, '!': Assembly.Calculate_1_Operand, '#': AddDigits.Calculate_1_Operand}


# a list of all the possible operators
OPERATORS_LIST = ['+', '-', '*', '/', '^', '%', '$', '&', '@', '~', '!', '#']

# a list of the operators that take only 1 operand
OPERATOR_FOR_1_OPERAND = ['~', '!', '#']