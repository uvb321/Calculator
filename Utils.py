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


def Make_Decimal_Values(lst: list) -> list:
    """
    this function gets a
    :param lst:
    :return:
    """
    i = 0
    while i < len(lst):
        if lst[i] == '.':
            lst.pop(i)
            before_point = lst.pop(i - 1)
            after_point = lst.pop(i - 1)
            i -= 1
            new_num = float(str(before_point) + '.' + str(after_point))
            lst.insert(i, new_num)
        i += 1

    return lst


def Reduce_And_Correct_Minuses(lst: list) -> list:
    """
    if there is an even amount of minuses in a row than the func deletes them and turns it into a '+',
    but if there is an odd amount of minuses the func also deletes them but insert a single '-' instead.
    this func uses two loop, the main one is to pass all of the values in the list and check if they are a '-', and if
    so it enters the second loop that counts how many minuses are in a row and deletes them.
    even though there is a loop inside of a loop the runtime complexity is O(N)
    :param lst: gets a list in regular order with many possibles minuses
    :return: returns the same list with compressed minuses
    """
    minus_cnt = 0
    minus_start_index = 0
    i = 0

    for item in lst:

        if item == '-':
            minus_cnt = 1
            minus_start_index = i

            lst.pop(minus_start_index)

            while len(lst) > minus_start_index and lst[minus_start_index] == '-':
                lst.pop(minus_start_index)
                minus_cnt += 1

            # if there is an even amount of minuses
            if minus_cnt % 2 == 0:
                # check if there is an operator before the start of the minuses, if so do nothing
                if not Is_Num(lst[minus_start_index - 1]):
                    pass  # deletes the minuses

                # else there is a number
                else:
                    lst.insert(minus_start_index, '+')

            # else there is an odd amount of minuses
            else:

                # check if there is an operator before the start of the minuses, or the minus is the first item
                if minus_start_index - 1 < 0 or not Is_Num(lst[minus_start_index - 1]):
                    # now its an unary minus, meaning it needs to be attached to the next expression
                    # it will be handled in the Turn_List_Order_To_Postfix function
                    if lst[minus_start_index] == '(':
                        lst.insert(minus_start_index, '-')

                    else:
                        lst[minus_start_index] = -lst[minus_start_index]

                # else there is a number
                else:
                    lst.insert(minus_start_index, '-')
        i += 1

    return lst


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


def Turn_String_To_List(data: str) -> list:
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
    this function  turns the list's order to postfix and it uses two help lists
    that one of them will operate as a stack.
    one stack will be for the operators and the other would be for the complete postfix expression.
    this function also handles a situation where there is an unary minus
    :param lst: gets a list that contains a regular order of the math expression
    :return: returns a list with the math expression in a postfix order
    """
    operators_stk = []
    new_lst = []

    minus_cnt = 0
    i = 0
    for item in lst:

        # if the item is a number append to the new list
        if Is_Num(item):
            new_lst.append(item)

        # else the item is an operator or ()
        else:
            # if there was an operator before the minus, its an unary minus and needs to be handled with
            if item == '-' and not Is_Num(lst[i - 1]):
                # appending 0 because 0 - expression = -expression
                new_lst.append(0)
                minus_cnt += 1


            elif item == '(':
                operators_stk.append(item)

            elif item == ')':
                operator = operators_stk.pop()
                while operator != '(':
                    new_lst.append(operator)
                    operator = operators_stk.pop()

                if minus_cnt > 0:
                    new_lst.append('-')
                    minus_cnt -= 1



            # if the item is not ( or ) than the item must be an operator
            else:
                # appending the operators from the stack as long as they have a higher order than the current operator
                # and the current top item is not ( and the stack isn't empty
                while len(operators_stk) > 0 and operators_stk[-1] != '(' \
                        and OPERATORS_ORDER[operators_stk[-1]] >= OPERATORS_ORDER[item]:
                    new_lst.append(operators_stk.pop())

                operators_stk.append(item)
        i += 1

    # at the end just append all of the remaining operators to the new list
    while len(operators_stk) > 0:
        new_lst.append(operators_stk.pop())

    return new_lst


def Calculate_Postfix(lst: list):
    """
    this func turns the postfix expression into a number
    :param data: data is the postfix expression
    :return: returns a number from the postfix expression
    """
    i = 0
    # if len data is 1 than the remaining item must be the answer
    while len(lst) > 1:
        # if item is operator
        if not Is_Num(lst[i]):
            operator = lst.pop(i)

            if operator in OPERATOR_FOR_1_OPERAND:
                num1 = lst.pop(i - 1)
                i -= 1

                num = OPERATORS_FUNCS[operator](num1)
                lst.insert(i, num)

            # if entered here the operator work with 2 operands
            else:
                num2 = lst.pop(i - 1)
                num1 = lst.pop(i - 2)
                i -= 2

                num = OPERATORS_FUNCS[operator](num1, num2)
                lst.insert(i, num)

        i += 1

    # returning the result of the math expression
    return lst[0]


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

    # after this line all of the minuses will be compressed to one '-' or turned into a '+'
    lst = Reduce_And_Correct_Minuses(lst)

    # after this line the list will return the numbers with decimal points
    lst = Make_Decimal_Values(lst)

    # now i turn this list to a list of with postfix order, so i don't have to deal with ()
    lst_in_postfix = Turn_List_Order_To_Postfix(lst)

    return Calculate_Postfix(lst_in_postfix)
