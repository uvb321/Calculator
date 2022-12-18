from CalculateFuncs import calculate
from Validation import validate
from Exceptions import *

QUIT = 'quit'


def run_calculator():
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
            # turning the expression to lower case
            expression = expression.lower()
            if expression == QUIT:
                break

            lst = validate(expression)
            num = calculate(lst)
            print(f"the result is: {num}")

        except DotException as DE:
            print(DE)

        except InputBracketsException as IBE:
            print(IBE)

        except InputException as IE:
            print(IE)

        except NegativeNumberException as NNE:
            print(NNE)

        except OperatorException as OE:
            print(OE)

        except FloatNumberException as FNE:
            print(FNE)

        except DivisionOrModuloByZeroException as DOMBZE:
            print(DOMBZE)

        except EmptyExpressionException as EEE:
            print(EEE)

        except ComplexNumberException as CNE:
            print(CNE)

        except EOFError:
            print("can't get EOF as input")
            break

        except Exception as E:
            print(E)
        finally:
            print("------------------------------------------\n\n\n")

    print("\n\n-----------------------------------------------------------------")
    print("closing Calculator")
