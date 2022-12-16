class InputLettersException(Exception):
    """
    raised when there are letters in the string
    """
    pass


class InputBracketsException(Exception):
    """
    raised when the number of '(' isn't equal to the number of ')'
    """
