from math import pow
from Exceptions import *

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
    def calculate_2_operands(num1, num2):
        pass

    # this func is meant to be overridden
    def calculate_1_operand(num):
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
    def calculate_2_operands(num1: float, num2: float):
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
    def calculate_2_operands(num1: float, num2: float) -> float:
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
    def calculate_2_operands(num1: float, num2: float) -> float:
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
    def calculate_2_operands(num1: float, num2: float) -> float:
        if num2 == 0:
            raise DivisionOrModuloByZeroException("can't do division by 0")
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
    def calculate_2_operands(num1: float, num2: float) -> float:
        if num1 == 0 and num2 == 0:
            raise OperatorException("can't do 0 in the power of 0.")
        try:
            return pow(num1, num2)
        except ValueError:
            raise ComplexNumberException("the result of ^ (power) can't be a complex number")


"""
this class is for the % sign
its order is 4
there is a modulo function
the operator will be between two operands num1 % num 2
"""


class Modulo(Operator):
    ORDER = 4

    # this func gets two numbers and returns the remainder from the division function on the two
    def calculate_2_operands(num1: float, num2: float) -> float:
        if num2 == 0:
            raise DivisionOrModuloByZeroException("can't do Modulo by 0")
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
    def calculate_2_operands(num1: float, num2: float) -> float:
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
    def calculate_2_operands(num1: float, num2: float) -> float:
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
    def calculate_2_operands(num1: float, num2: float) -> float:
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
    def calculate_1_operand(num: float) -> float:
        return -num


"""
this class is for the ! sign
its order is 6
there is an assembly function
the operator will be right of the operand num!

"""

# a const to change if the computer can calculate to a different limit of assembly
CEILING_FOR_ASSEMBLY = 170


class Assembly(Operator):
    ORDER = 6

    # this func gets a number and returns the  assembly of it
    # works only on a positive natural number
    def calculate_1_operand(num: int) -> int:
        if num > CEILING_FOR_ASSEMBLY:
            raise TooHighToCalculateException(f" the ! function can't handle a number over {CEILING_FOR_ASSEMBLY}")

        if type(num) == float:
            # getting the number after the decimal point
            after_decimal_point = int(str(num).split('.')[-1])

            # checking if the number is not natural
            if after_decimal_point > 0:
                raise FloatNumberException("! can't get a real number as operand")

        # checking is the number is negative
        if num < 0:
            raise NegativeNumberException("! can't get a negative number as operand")

        # casting
        num = int(num)
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
    def calculate_1_operand(num: float) -> int:
        # checking if the number is negative
        negative_flag = False
        if num < 0:
            negative_flag = True
        # this line will put in places how many digits there are after the decimal point
        places = len(str(num).split('.')[-1])

        # this line will make num an int with all of its digits
        for i in range(places):
            num *= 10

        # if it was negative in the beginning than making it positive
        if negative_flag:
            num *= -1

        # a loop that sums the digits of the number
        digits_sum = 0
        while num:
            digits_sum += num % 10
            num //= 10

        # if it was negative in the beginning than making it negative again
        if negative_flag:
            digits_sum *= -1
        return digits_sum
