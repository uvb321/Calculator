from Exceptions import *
from Operators import *
from Dicts_And_Lists import *



def Make_Decimal_Values(lst: list) -> list:
    """
    this function gets a
    :param lst:
    :return:
    """
    index = 0
    while index < len(lst):
        if lst[index] == '.':
            lst.pop(index)
            before_point = lst.pop(index - 1)
            after_point = lst.pop(index - 1)
            index -= 1
            try:
                new_num = float(str(before_point) + '.' + str(after_point))
            except ValueError:
                raise DotError("the dots are not in a valid order")
            lst.insert(index, new_num)
        index += 1

    return lst


def Reduce_And_Correct_Minuses(lst: list) -> list:
    """
    if there is an even amount of minuses in a row than the func deletes them and turns it into a '+',
    but if there is an odd amount of minuses the func also deletes them but insert a single '-' instead.
    this func uses two loops, the main one is to check all of the values in the list and check if they are a '-', and if
    so it enters the second loop that counts how many minuses are in a row and deletes them.
    even though there is a loop inside of a loop the runtime complexity is O(N)
    :param lst: gets a list in regular order with many possibles minuses
    :return: returns the same list with compressed minuses
    """
    minus_cnt = 0
    minus_start_index = 0
    index = 0

    for item in lst:

        if item == '-':
            minus_cnt = 1
            minus_start_index = index

            lst.pop(minus_start_index)

            # a loop that gets all of the minuses out of the list and counts them
            while len(lst) > minus_start_index and lst[minus_start_index] == '-':
                lst.pop(minus_start_index)
                minus_cnt += 1

            after = lst[minus_start_index]
            prev = lst[minus_start_index - 1]

            # if there is an even amount of minuses
            if minus_cnt % 2 == 0:
                # if index is 0, than minuses at the start so delete them

                if minus_start_index == 0 or prev == '(':
                    pass

                # if the item after is not a number and it's not a '('
                elif not Is_Num(after) and after != '(':
                    # deletes the pluses
                    pass

                # else there is a number
                else:
                    # entering a + instead
                    lst.insert(minus_start_index, '+')

            # else there is an odd amount of minuses
            else:
                # if there is a number after the minuses
                if (minus_start_index == 0 or prev == '(') and Is_Num(after):
                    # converting the number to its opposite
                    lst[minus_start_index] = -lst[minus_start_index]

                # if the previous is an operator and after is a number
                elif prev in OPERATORS_LIST and Is_Num(after):
                    # here there are 2 cases, either the - is counted as unary or binary
                    if prev in OPERATOR_FOR_1_OPERAND and prev != '~':
                        # here the prev is either ! or #
                        lst.insert(minus_start_index, '-')

                    else:
                        # every other operator is fine
                        lst[minus_start_index] = -lst[minus_start_index]

                else:
                    # entering a single -
                    lst.insert(minus_start_index, '-')

        index += 1

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

    # a helpful sub string that help with converting to a number from string
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


def Make_List(expression: str) -> list:
    """
    this function takes a string that represents a math expression, shrinks it's spaces and minuses
    and turns the number into their real values
    :param expression: a string that represents a math expression
    :return: a list that represents the same math expression
    """

    # turning the string into a list
    lst = Turn_String_To_List(expression)

    # after this line all of the minuses will be compressed to one '-' or turned into a '+'
    lst = Reduce_And_Correct_Minuses(lst)

    # after this line the list will return the numbers with decimal points
    lst = Make_Decimal_Values(lst)

    return lst
