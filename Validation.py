from Exceptions import *
from Operators import *
# using the operator list from the utils file
from Utils import Make_List, Is_Num
from Dicts_And_Lists import *


def Check_For_Wrong_Input(expression: str):
    """
    this function runs a loop that checks each char
    :param expression: an string that represents a math expression
    :return: nothing, if expression isn't valid error will be raised
    """
    # at the end if the brackets cnt isn't 0, than error is raised
    brackets_cnt = 0
    # index to help with finding where is the mistake
    index = 0
    for char in expression:

        if char == '(':
            brackets_cnt += 1
            # checking if the brackets are empty
            if expression[index + 1] == ')':
                raise InputBracketsException(f"the () in the {index + 1} place can't be empty ")

        elif char == ')':
            brackets_cnt -= 1
            # ) can't come before a ( so if the counter goes below 0 an error is raised
            if brackets_cnt < 0:
                raise InputBracketsException(f" the ) in the {index + 1} place can't come before a (")

        # checking if the char is a .

        elif char == '.':
            # if so checking if it is the first
            # char or the char before it isn't a number,
            # if it is the case raising an error
            if index - 1 < 0 or not expression[index - 1].isdigit():
                raise DotError(f"the . in the {index + 1} place does not have a number before it")

        # finally checking of the char is not an operator or a digit
        elif char not in OPERATORS_LIST and not char.isdigit():
            raise InputError(f"the char ({char}) in the {index + 1} place is illegal")

        index += 1

    # checking if there are  more ( (openers) than ) (closers)
    if brackets_cnt > 0:
        raise InputBracketsException(f"the ( does not have a corresponding closing )")


def Validate_Uniqe_Operators(lst: list):
    """
    the unique operators are the i=ones that take 1 operand instead of two
    :param lst: a list that represents a math expression
    :return: raises an error if there is something wrong in the expression
    """
    index = 0
    for item in lst:
        if item in OPERATOR_FOR_1_OPERAND:
            # if the item is in the list of special operators than there are two cases
            if item == '!' or item == '#':
                # if the ! is in the first place, or the expression before it isn't a number and it isn't a (
                # and its not an operator that takes one operand that it's in the wrong place
                if index == 0 or (not Is_Num(lst[index - 1]) and lst[index - 1] != '(' and lst[
                    index - 1] not in OPERATOR_FOR_1_OPERAND):
                    raise WrongOrderException(f"the {item} in the {index + 1} place does not come after an expression")

            elif item == '~':
                # if its the last item or the item after it isn't a number and it isn't a '(' than it in the
                # wrong place
                if index + 1 == len(lst) or (not Is_Num(lst[index + 1]) and lst[index + 1] != '('):
                    raise WrongOrderException(f"the {item} in the {index + 1} place does not come before an expression")
        index += 1


def Validate(expression: str) -> list:
    """
    this function gathers all of the other functions in this file
    :param expression: the string from the user that represents a math expression
    :return: true if the math expression is valid, false otherwise
    """

    # removing all of the spaces in the string
    expression = expression.replace(' ', '')

    if expression == "":
        raise EmptyExpressionException("the input can't be empty")

    # checking the expression
    Check_For_Wrong_Input(expression)

    # making a list out of the expression
    lst = Make_List(expression)

    # checking the unique operators in the lst
    Validate_Uniqe_Operators(lst)

    # returning a list that represents a
    return lst
