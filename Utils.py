from Dicts_And_Lists import *


def make_decimal_values(lst: list) -> list:
    """
    this function gets a list and turns all of the float numbers to their real value
    :param lst: gets a list that represents a math expression
    :return: returns the same list with decimal numbers
    """
    index = 0
    while index < len(lst):
        if lst[index] == '.':
            # popping out the .
            lst.pop(index)
            # popping the numbers before and after the .
            before_point = lst.pop(index - 1)
            after_point = lst.pop(index - 1)
            index -= 1
            try:
                new_num = float(str(before_point) + '.' + str(after_point))
            except ValueError:
                raise DotException("the dots are not in a valid order")
            # inserting the new decimal number to the lst
            lst.insert(index, new_num)
        index += 1

    return lst


def reduce_and_correct_minuses(lst: list) -> list:
    """
    if there is an even amount of minuses in a row than the func deletes them and turns it into a '+',
    but if there is an odd amount of minuses the func also deletes them but insert a single '-' instead.
    this func uses two loops, the main one is to check all of the values in the list and check if they are a '-', and if
    so it enters the second loop that counts how many minuses are in a row and deletes them.
    even though there is a loop inside of a loop the runtime complexity is O(N)
    :param lst: gets a list in regular order with many possibles minuses
    :return: returns the same list with compressed minuses
    """

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

            # check if the minuses end the expression and if so raise an exception
            if minus_start_index >= len(lst):
                raise OperatorException("- can't be at the end of an expression")
            after = lst[minus_start_index]
            prev = lst[minus_start_index - 1]

            # if there is an even amount of minuses
            if minus_cnt % 2 == 0:
                # if index is 0, than minuses at the start so delete them

                if minus_start_index == 0 or prev == '(':
                    pass

                # if the item after is not a number and it's not a '(' and it's not a '~'
                elif not is_num(after) and after != '(' and after != '~':
                    # deletes the pluses
                    pass
                elif prev in OPERATORS_LIST:
                    if prev in OPERATOR_FOR_1_OPERAND and prev != '~':
                        lst.insert(minus_start_index, '+')
                    else:
                        # deletes the minuses
                        pass
                # else there is a number
                else:
                    # entering a + instead
                    lst.insert(minus_start_index, '+')

            # else there is an odd amount of minuses
            else:
                # if there is a number after the minuses
                if (minus_start_index == 0 or prev == '(') and is_num(after):
                    # converting the number to its opposite
                    lst[minus_start_index] = -lst[minus_start_index]

                # if the previous is an operator and after is a number
                elif prev in OPERATORS_LIST and is_num(after):
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


def from_string_to_num(data: str) -> float:
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


def is_operand(data: chr) -> bool:
    """
    this function gets a char and returns if the char represents a digit
    :param data: a char
    :return: if the char is a char that represents a number
    """
    return '0' <= data <= '9'


def is_num(item) -> bool:
    """
    this func returns if an item is of type number
    :param item: gets an item of a list
    :return: true if the data is of a number type, else returns false
    """
    return type(item) is int or type(item) is float


def turn_numbers_to_value(lst: list) -> list:
    """
    this func runs on each character in the string and appends it to a list, if a sequence of chars represents
    a number than the func appends the real value of the number to the list and not its chars
    :param lst: it takes the list with no spaces and turns the numbers into their real value and not
    chars
    :return: it returns a list with the same order of the expression only that every single num or operator is an
    item in the list so it will be easier to work with
    """
    # this list will help me calculate the expression
    new_lst = []

    # a helpful sub string that help with converting to a number from string
    sub_str = ""

    # first of we push the string's simplified form to the stack
    for val in lst:

        # if the value is an operand than connect it to the sub string
        if is_operand(val):
            sub_str += val

        # if it's not an operand and the sub_str isn't empty than convert the sub_string into a number
        else:
            if sub_str != "":
                curr_num = from_string_to_num(sub_str)
                new_lst.append(curr_num)
            new_lst.append(val)
            sub_str = ""

    # if the last part of the data was a number we need to insert it to the stack
    if sub_str != "":
        curr_num = from_string_to_num(sub_str)
        new_lst.append(curr_num)

    return new_lst


def make_list(expression: list) -> list:
    """
    this function takes a string that represents a math expression, shrinks it's spaces and minuses
    and turns the number into their real values
    :param expression: a string that represents a math expression
    :return: a list that represents the same math expression
    """

    # turning the string of operands into their value
    lst = turn_numbers_to_value(expression)

    # after this line all of the minuses will be compressed to one '-' or turned into a '+'
    lst = reduce_and_correct_minuses(lst)

    # after this line the list will return the numbers with decimal points
    lst = make_decimal_values(lst)

    return lst
