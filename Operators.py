from math import pow

"""
this module contains all of the classes of the operators and the code of their functions
"""

"""
this is the father class to all of the operators 
there is an ORDER value the is supposed to be overridden
and there are also two kinds of function, one that gets two operands as parameters
and one that gets only one operand as parameter
"""


class Operator:
    # meant to be overridden
    ORDER = None

    # this func is meant to be overridden
    def Calculate_2_Operands(num1, num2):
        pass

    # this func is meant to be overridden
    def Calculate_1_Operand(num):
        pass


"""
this class is for the + sign
its order is 1
there is an addition function
the operator will be between two operands num1 + num 2
"""


class Add(Operator):
    ORDER = 1

    # this func gets two numbers and adds them and returns the result
    def Calculate_2_Operands(num1: float, num2: float):
        return num1 + num2


"""
this class is for the - sign
its order is 1
there is a subtraction function
the operator will be between two operands num1 - num 2
"""


class Sub(Operator):
    ORDER = 1

    # this func gets two numbers and subtracts the second from the first and returns the result
    def Calculate_2_Operands(num1: float, num2: float) -> float:
        return num1 - num2


"""
this class is for the * sign
its order is 2
there is a multiply function
the operator will be between two operands num1 * num 2
"""


class Mul(Operator):
    ORDER = 2

    # this func gets two numbers and multiplies them and returns the result
    def Calculate_2_Operands(num1: float, num2: float) -> float:
        return num1 * num2


"""
this class is for the / sign
its order is 2
there is a divide function
the operator will be between two operands num1 / num 2
"""


class Div(Operator):
    ORDER = 2

    # this func gets two numbers and divides the first with the second and returns the result
    def Calculate_2_Operands(num1: float, num2: float) -> float:
        return num1 / num2


"""
this class is for the ^ sign
its order is 3
there is a power function
the operator will be between two operands num1 ^ num 2
"""


class Pow(Operator):
    ORDER = 3

    # this func gets two numbers and powers the first with the second and returns the result
    def Calculate_2_Operands(num1: float, num2: float) -> float:
        return pow(num1, num2)


"""
this class is for the % sign
its order is 4
there is a modulu function
the operator will be between two operands num1 % num 2
"""


class Modulu(Operator):
    ORDER = 4

    # this func gets two numbers and returns the remainder from the division function on the two
    def Calculate_2_Operands(num1: float, num2: float) -> float:
        return num1 % num2


"""
this class is for the $ sign
its order is 5
there is a max function
the operator will be between two operands num1 $ num 2
"""


class Max(Operator):
    ORDER = 5

    # this func gets two numbers and returns the bigger one out of the two
    def Calculate_2_Operands(num1: float, num2: float) -> float:
        if num1 > num2:
            return num1
        return num2


"""
this class is for the & sign
its order is 5
there is a min function
the operator will be between two operands num1 & num 2
"""


class Min(Operator):
    ORDER = 5

    # this func gets two numbers and returns the smaller one out of the two
    def Calculate_2_Operands(num1: float, num2: float) -> float:
        if num1 < num2:
            return num1
        return num2


"""
this class is for the @ sign
its order is 5
there is an average function
the operator will be between two operands num1 @ num 2
"""


class Avg(Operator):
    ORDER = 5

    # this func gets two numbers and returns their average
    def Calculate_2_Operands(num1: float, num2: float) -> float:
        return (num1 + num2) / 2


"""
this class is for the ~ sign
its order is 6
there is a not function
the operator will be left of the operand ~num

"""


class Not(Operator):
    ORDER = 6

    # this func gets a number and returns the opposite sign of it
    def Calculate_1_Operand(num: float) -> float:
        return -num


"""
this class is for the ! sign
its order is 6
there is an assembly function
the operator will be right of the operand num!

"""


class Assembly(Operator):
    ORDER = 6

    # this func gets a number and returns the  assembly of it
    # works only on a positive WHOLE number!!!
    def Calculate_1_Operand(num: int) -> int:
        sum = 1
        # loop until the num is 1
        while num > 1:
            # multiplying sum with current num and updating sum
            sum *= num
            num -= 1

        # returning sum
        return sum


"""
this class is for the # sign
its order is 6
there is an AddDigits function
the operator will be right of the operand num#

"""


class AddDigits(Operator):
    ORDER = 6

    # this func gets a num and returns the sum of its digits
    # works only on a positive number!!!
    def Calculate_1_Operand(num: float) -> int:
        # this line will put in places how many digits there are after the decimal point
        places = len(str(num).split('.')[-1])
        # this line will make num an int with all of its digits
        num = int(num * pow(10, places))

        sum = 0
        while num:
            sum += num % 10
            num //= 10
        return sum
