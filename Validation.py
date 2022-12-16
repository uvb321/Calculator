from Exceptions import *


def Check_For_Wrong_Input(expression: str):
    # at the end if the brackets cnt isn't 0, than error is raised
    brackets_cnt = 0
    # index to help with finding where is the mistake
    i = 0
    try:
        for char in expression:
            if char.isalpha():
                raise InputLettersException(f"there is a letter in the {i+1} place: {char}")

            elif char == '(':
                brackets_cnt += 1

            elif char == ')':
                brackets_cnt -= 1
                if brackets_cnt < 0:
                    raise InputBracketsException(f" the ) in the {i+1} place can't come before a (")

    except InputLettersException as ILE:
        print(ILE)

    except InputBracketsException as IBE:
        print(IBE)


def Validate(expression: str):
    Check_For_Wrong_Input(expression)
