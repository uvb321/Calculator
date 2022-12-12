from Operators import *

DICT = {'+': Add.Calculate_2_Operands, '-': Sub.Calculate_2_Operands, '*': Mul.Calculate_2_Operands,
        '/': Div.Calculate_2_Operands, '^': Pow.Calculate_2_Operands, '%': Modulu.Calculate_2_Operands,
        '$': Max.Calculate_2_Operands, '&': Min.Calculate_2_Operands, '@': Avg.Calculate_2_Operands,
        '~': Not.Calculate_1_Operand, '!': Assembly.Calculate_1_Operand, '#': AddDigits.Calculate_1_Operand}


def Reduce_Minuses(data: str):
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


def calculate(data: str):
    # this list will help me calculate the expression
    lst = []

    # removing all of the spaces in the string
    data = data.replace(' ', '')

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

    # right now we have a list that is organized

