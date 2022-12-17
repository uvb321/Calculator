class InputBracketsException(Exception):
    """
    raised when the number of '(' isn't equal to the number of ')'
    """


class InputError(Exception):
    """
    raised when there is an unknown char in the string that represents the math expression
    """


class DotError(Exception):
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


class NotEnoughOperandsForActionException(Exception):
    """
    raised when there is not enough operands to complete the action
    """


class GotNoOperatorException(Exception):
    """
    raised when there is no operator for the operands
    """


class EmptyExpressionException(Exception):
    """
    raised when there is no expression to work with
    """


class DivisionByZeroException(Exception):
    """
    raised when there is a division by zero
    """


class WrongOrderException(Exception):
    """
    raised when the special operators are not in the  correct place
    """
