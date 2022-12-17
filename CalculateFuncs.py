from Operators import *
from Exceptions import *
from Utils import Is_Num
from Dicts_And_Lists import *


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

    # helpful index for the loop
    index = 0
    # stack to help with unary minuses of expressions in ()
    minus_stk = []
    for item in lst:

        # if the item is a number append to the new list
        if Is_Num(item):
            new_lst.append(item)

        # else the item is an operator or ()
        else:

            # if there is a minus and the item after is a '(' and the item before it is an operator, or the minuses
            # start the expression
            # than it needs to be attached to the () that comes after it
            if item == '-' and index + 1 < len(lst) and lst[index + 1] == '(' \
                    and ((index - 1 < 0) or (
                    index - 1 >= 0 and (lst[index - 1] in OPERATORS_LIST or lst[index - 1] == '('))):
                # at this point the only times where a special action needs to occur is in 2 situations
                # number 1: if the minuses are at the beginning.
                # number 2: if there is an operator before the minus
                # pushing 0 to later do 0-expression
                new_lst.append(0)
                minus_stk.append('-')

            elif item == '(':
                operators_stk.append(item)
                # pushing '(' to the minus stack to know which of the () has a minus in front of it
                minus_stk.append('(')

            elif item == ')':
                operator = operators_stk.pop()
                while operator != '(':
                    new_lst.append(operator)
                    operator = operators_stk.pop()

                # popping out the '('
                minus_stk.pop()
                if len(minus_stk) > 0 and minus_stk[-1] == '-':
                    # adding a minus
                    # deleting the minus so it won't do it again
                    new_lst.append(minus_stk.pop())

            # if the item is not ( or ) than the item must be an operator
            else:
                # appending the operators from the stack as long as they have a higher order than the current operator
                # and the current top item is not ( and the stack isn't empty
                while len(operators_stk) > 0 and operators_stk[-1] != '(' \
                        and OPERATORS_ORDER[operators_stk[-1]] >= OPERATORS_ORDER[item]:
                    new_lst.append(operators_stk.pop())

                operators_stk.append(item)
        index += 1

    # at the end just append all of the remaining operators to the new list
    while len(operators_stk) > 0:
        new_lst.append(operators_stk.pop())

    return new_lst


def Calculate_Postfix(lst: list):
    """
    this func turns the postfix expression into a number
    :param lst: lst is the postfix expression
    :return: returns a number from the postfix expression
    """
    index = 0
    # if len data is 1 than the remaining item must be the answer
    while len(lst) > 1:
        # check if the index is bigger than the length of the list
        # if so it means that there are more operands than operators to do actions with
        if index == len(lst):
            raise GotNoOperatorException("not enough operators to do actions with")
        # if item is operator
        if not Is_Num(lst[index]):
            operator = lst.pop(index)

            if operator in OPERATOR_FOR_1_OPERAND:
                if index - 1 < 0:
                    raise NotEnoughOperandsForActionException(f"the operator {operator} did not get any operands")
                num1 = lst.pop(index - 1)
                index -= 1

                num = OPERATORS_FUNCS[operator](num1)
                lst.insert(index, num)

            # if entered here the operator work with 2 operands
            else:
                if index - 2 < 0:
                    raise NotEnoughOperandsForActionException(f"the operator {operator} takes 2 operands")
                num2 = lst.pop(index - 1)
                num1 = lst.pop(index - 2)
                index -= 2

                num = OPERATORS_FUNCS[operator](num1, num2)
                lst.insert(index, num)

        index += 1

    # returning the result of the math expression
    return lst[0]


def Calculate(lst: list):
    """
    this function gathers all of the other functions in this file and uses them by order to turn a list that
    represents a math expression into a number
    :param lst: a list that represents a math expression
    :return: the result of the math expression
    """

    # now i turn this list to a list of with postfix order, so i don't have to deal with ()
    lst_in_postfix = Turn_List_Order_To_Postfix(lst)

    return Calculate_Postfix(lst_in_postfix)
