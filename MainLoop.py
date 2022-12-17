from CalculateFuncs import Calculate
from Validation import Validate
from Exceptions import *

QUIT = 'quit'


def Run_Calculator():
    """
    this method is the main loop of the calculator, in this loop there is the input of the math expression
    and the sending of this string to the functions that calculate it
    :return:
    """
    """
    """
    while True:
        print("------------------------------------------")
        try:
            expression = input("please enter a math expression:\n ")
            if expression == QUIT:
                break

            lst = Validate(expression)
            num = Calculate(lst)
            print(f"the result is: {num}")

        except DotError as DE:
            print(DE)

        except InputBracketsException as IBE:
            print(IBE)

        except InputError as IE:
            print(IE)

        except NegativeNumberException as NNE:
            print(NNE)

        except NotEnoughOperandsForActionException as NEOFAE:
            print(NEOFAE)

        except GotNoOperatorException as GNOE:
            print(GNOE)

        except FloatNumberException as FNE:
            print(FNE)

        except DivisionByZeroException as DBZE:
            print(DBZE)

        except WrongOrderException as WOE:
            print(WOE)

        except EmptyExpressionException as EEE:
            print(EEE)

        except EOFError:
            print("can't get EOF as input")

            # todo: fix the EOF error

        except Exception as E:
            print(E)
        finally:
            print("------------------------------------------\n\n\n")

    print("\n\n-----------------------------------------------------------------")
    print("closing Calculator")
