from Utils import Calculate

QUIT = 'quit'

def Run_Calculator():
    expression = input("please enter a math expression:\n ")
    while expression != QUIT:
        print("------------------------------------------")
        num = Calculate(expression)
        print(f"the result is: {num}")
        print("------------------------------------------\n\n\n")
        expression = input("please enter a math expression:\n ")


    print("closing Calculator")

def main():
    pass


if __name__ == '__main__':
    main()
