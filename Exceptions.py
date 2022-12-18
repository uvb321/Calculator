"""
this file consists all of the custom exceptions that are caught in the main loop
"""


class InputBracketsException(Exception):
    """
    raised when the number of '(' isn't equal to the number of ')'
    """


class InputException(Exception):
    """
    raised when there is an unknown char in the string that represents the math expression
    """


class DotException(Exception):
    """
    raised when there isn't a number before a point
    """


class NegativeNumberException(Exception):
    """
    raised when an operator that can't work with negative numbers gets a negative number
    """


class FloatNumberException(Exception):
    """
    raised when an operator that can't work with real numbers gets a real number
    """


class EmptyExpressionException(Exception):
    """
    raised when there is no expression to work with
    """


class DivisionOrModuloByZeroException(Exception):
    """
    raised when there is a division by zero
    """


class ComplexNumberException(Exception):
    """
    raised when the result of the power is a comlex number
    """


class TooHighToCalculateException(Exception):
    """
    raised when the number is too high to do calculations on
    """


class OperatorException(Exception):
    """
    raised when there is a problem with an operator
    """
