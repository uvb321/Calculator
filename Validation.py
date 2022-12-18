from Utils import make_list, is_num
from Dicts_And_Lists import *


def check_for_wrong_input(expression: list):
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
                raise DotException(f"the . in the {index + 1} place does not have a number before it")

        # finally checking of the char is not an operator or a digit
        elif char not in OPERATORS_LIST and not char.isdigit():
            raise InputException(f"the char ({char}) in the {index + 1} place is illegal")

        index += 1

    # checking if there are  more ( (openers) than ) (closers)
    if brackets_cnt > 0:
        raise InputBracketsException(f"the ( does not have a corresponding closing )")


def validate_operators(lst: list):
    """
    this functions tells if the operators are valid
    :param lst: a list that represents a math expression
    :return: raises an error if there is something wrong in the expression
    """
    index = 0
    for item in lst:
        if item in OPERATORS_LIST:
            prev = lst[index - 1]
            # if the item is in the list of special operators than there are two cases
            if item in OPERATOR_FOR_1_OPERAND:
                if item == '!' or item == '#':
                    # if the ! is in the first place, or the expression before it isn't a number and it isn't a (
                    # and its not an operator that takes one operand that it's in the wrong place
                    if index == 0 or (not is_num(prev) and prev != ')' and prev not in OPERATOR_FOR_1_OPERAND):
                        raise OperatorException(
                            f"the {item} in the {index + 1} place does not come after an expression")

                elif item == '~':
                    # if its the last item or the item after it isn't a number and it isn't a '(' than it in the
                    # wrong place
                    if index + 1 == len(lst) or (
                            not is_num(lst[index + 1]) and lst[index + 1] != '(' and lst[index + 1] != '-'):
                        raise OperatorException(
                            f"the {item} in the {index + 1} place does not come before an expression")
            # else its a regular operator and it takes 2 operands
            else:
                if index + 1 == len(lst):
                    raise OperatorException(f"the {item} can't be in the end")
                if index == 0 and item != '-':
                    raise OperatorException(f"the {item} can't be in the beginning")

                after = lst[index + 1]
                # '-' is a special operand and dealt with later
                if item != '-':
                    # if the item before the operator is not number, and it's not a ')' and it's not an operator
                    # or the number after it isn't a number and it's not a '(' and it's not a '-' and it's not a '~'
                    if (not is_num(prev) and prev != ')' and prev not in OPERATORS_LIST) or (
                            not is_num(after) and after != '(' and after != '-' and after != '~'):
                        raise OperatorException(f"the {item} in the {index + 1} place must take 2 operands")


        index += 1


def validate(expression: str) -> list:
    """
    this function gathers all of the other functions in this file
    :param expression: the string from the user that represents a math expression
    :return: true if the math expression is valid, false otherwise
    """

    # removing all of the spaces in the string
    expression = [ch for ch in expression if not ch.isspace()]

    # checking if the list is empty
    if not expression:
        raise EmptyExpressionException("the input can't be empty")

    # checking the expression for wrong input
    check_for_wrong_input(expression)

    # making a corrected list out of the expression
    lst = make_list(expression)

    # validating the operators in the lst
    validate_operators(lst)

    # returning a list that represents a
    return lst
