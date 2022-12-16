from Utils import Calculate
from Validation import Validate

QUIT = 'quit'

def Run_Calculator():
    expression = input("please enter a math expression:\n ")
    while expression != QUIT:
        Validate(expression)
        print("------------------------------------------")
        num = Calculate(expression)
        print(f"the result is: {num}")
        print("------------------------------------------\n\n\n")
        expression = input("please enter a math expression:\n ")


    print("closing Calculator")

