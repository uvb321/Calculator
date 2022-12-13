from Operators import *

OPERATORS_FUNCS = {'+': Add.Calculate_2_Operands, '-': Sub.Calculate_2_Operands, '*': Mul.Calculate_2_Operands,
                   '/': Div.Calculate_2_Operands, '^': Pow.Calculate_2_Operands, '%': Modulu.Calculate_2_Operands,
                   '$': Max.Calculate_2_Operands, '&': Min.Calculate_2_Operands, '@': Avg.Calculate_2_Operands,
                   '~': Not.Calculate_1_Operand, '!': Assembly.Calculate_1_Operand, '#': AddDigits.Calculate_1_Operand}

OPERATORS_ORDER = {'+': Add.ORDER, '-': Sub.ORDER, '*': Mul.ORDER,
                   '/': Div.ORDER, '^': Pow.ORDER, '%': Modulu.ORDER,
                   '$': Max.ORDER, '&': Min.ORDER, '@': Avg.ORDER, '~': Not.ORDER,
                   '!': Assembly.ORDER, '#': AddDigits.ORDER}

OPERATORS_LIST = ['+', '-', '*', '/', '^', '%', '$', '&', '@', '~', '!', '#']

OPERATOR_FOR_1_OPERAND = ['~', '!', '#']


def Reduce_Minuses(data: list) -> list:
    # todo: complete this function
    pass


def From_String_To_Num(data: str) -> float:
    """
    this function runs on the chars of the string and turn each of them to a number and puts the number together
    :param data: a string that represents a number
    :return: the value of the number
    """

    num = 0
    for char in data:
        num *= 10
        num += int(char) - int('0')

    return num


def Is_Opernad(data: chr) -> bool:
    """
    this function gets a char and returns if the char represents a digit
    :param data: a char
    :return: if the char is a char that represents a number
    """
    return data <= '9' and data >= '0'


def Is_Num(item) -> bool:
    """
    this func returns if an item is of type number
    :param item: gets an item of a list
    :return: true if the data is of a number type, else returns false
    """
    return type(item) is int or type(item) is float


def Turn_String_To_List(data) -> list:
    """
    this func runs on each character in the string and appends it to a list, if a sequence of chars represents
    a number than the func appends the real value of the number to the list and not its chars
    :param data: it takes the string with no spaces and turns the numbers into their real value and not
    charcters
    :return: it returns a list with the same order of the expression only that every single num or operator is an
    item in the list so it will be easier to work with
    """
    # this list will help me calculate the expression
    lst = []

    subStr = ""

    # first of we push the string's simplified form to the stack
    for val in data:

        if Is_Opernad(val):
            subStr += val

        else:
            currNum = 0
            if subStr != "":
                currNum = From_String_To_Num(subStr)
                lst.append(currNum)
            lst.append(val)
            subStr = ""

    # if the last part of the data was a number we need to insert it to the stack
    if subStr != "":
        currNum = From_String_To_Num(subStr)
        lst.append(currNum)

    return lst


def Turn_List_Order_To_Postfix(lst: list) -> list:
    """
    in this func i turn the list's order to postfix and i use two help lists that one of them will operate as a stack.
    one stack will be for the operators and the other would be for the complete postfix expression
    :param lst: gets a list that contains a regular order of the math expression
    :return: returns a list with the math expression in a postfix order
    """
    operators_stk = []
    new_lst = []

    for item in lst:
        # if the item is a number append to the new list
        if Is_Num(item):
            new_lst.append(item)

        # else the item is an operator or ()
        else:
            if item == '(':
                operators_stk.append(item)

            elif item == ')':
                operator = operators_stk.pop()
                while operator != '(':
                    new_lst.append(operator)
                    operator = operators_stk.pop()

            # if the item is not ( or ) than the item must be an operator
            else:
                # appending the operators from the stack as long as they have a higher order than the current operator
                # and the current top item is not ( and the stack isn't empty
                while len(operators_stk) > 0 and operators_stk[-1] != '(' \
                        and OPERATORS_ORDER[operators_stk[-1]] >= OPERATORS_ORDER[item]:
                    new_lst.append(operators_stk.pop())

                operators_stk.append(item)

    # at the end just append all of the remaining operators to the new list
    while len(operators_stk) > 0:
        new_lst.append(operators_stk.pop())

    return new_lst


def Calculate_Postfix(data: list):
    """
    this func turns the postfix expression into a number
    :param data: data is the postfix expression
    :return: returns a number from the postfix expression
    """
    i = 0
    # if len data is 1 than the remaining item must be the answer
    while len(data) > 1:
        # if item is operator
        if not Is_Num(data[i]):
            operator = data.pop(i)

            if operator in OPERATOR_FOR_1_OPERAND:
                pass
                # todo: needs to be completed

            # if entered here the operator work with 2 operands
            else:
                num2 = data.pop(i - 1)
                num1 = data.pop(i - 2)
                i -= 2

                num = OPERATORS_FUNCS[operator](num1, num2)
                data.insert(i, num)

        i += 1

    return data[0]


def Calculate(data: str):
    """
    this func gathers all of the other functions in this file and uses them by order to turn a string that
    represents a math expression into a number
    :param data: a string that represents a math expression
    :return: the result of the math expression
    """
    # removing all of the spaces in the string
    data = data.replace(' ', '')

    # right now we have a list that is organized
    lst = Turn_String_To_List(data)

    #lst = Reduce_Minuses(lst)

    # now i turn this list to a list of with postfix order, so i don't have to deal with ()
    lst_in_postfix = Turn_List_Order_To_Postfix(lst)

    return Calculate_Postfix(lst_in_postfix)
