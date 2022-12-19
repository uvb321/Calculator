import pytest
from Exceptions import *
from Validation import validate
from CalculateFuncs import calculate


def test_5_simple_errors():
    with pytest.raises(OperatorException):
        lst = validate("5-")
        calculate(lst)

    with pytest.raises(OperatorException):
        lst = validate("3*+2")
        calculate(lst)

    with pytest.raises(OperatorException):
        lst = validate("+3")
        calculate(lst)

    with pytest.raises(OperatorException):
        lst = validate("22^-")
        calculate(lst)

    with pytest.raises(DotException):
        lst = validate("5.2.4-3.6")
        calculate(lst)


def test_jibrish():
    with pytest.raises(InputException):
        validate("hjtrofjmrvrv")


def test_empty_expression():
    with pytest.raises(EmptyExpressionException):
        validate("")


def test_white_spaces():
    with pytest.raises(EmptyExpressionException):
        validate("                        ")


def test_simple_expressions():
    # 1
    lst = validate("3-2")
    num = calculate(lst)
    assert num == 1

    # 2
    lst = validate("2^3")
    num = calculate(lst)
    assert num == 8

    # 3
    lst = validate("5+3")
    num = calculate(lst)
    assert num == 8

    # 4
    lst = validate("2@10")
    num = calculate(lst)
    assert num == 6

    # 5
    lst = validate("2*1.5")
    num = calculate(lst)
    assert num == 3

    # 6
    lst = validate("10%3")
    num = calculate(lst)
    assert num == 1

    # 7
    lst = validate("90&-5")
    num = calculate(lst)
    assert num == -5

    # 8
    lst = validate("90$-5")
    num = calculate(lst)
    assert num == 90

    # 9
    lst = validate("~3")
    num = calculate(lst)
    assert num == -3

    # 10
    lst = validate("3!")
    num = calculate(lst)
    assert num == 6

    # 11
    lst = validate("123#")
    num = calculate(lst)
    assert num == 6

    # 12
    lst = validate("10/2")
    num = calculate(lst)
    assert num == 5

    # 13
    lst = validate("2--28")
    num = calculate(lst)
    assert num == 30

    # 14
    lst = validate("~(5*2)")
    num = calculate(lst)
    assert num == -10

    # 15
    lst = validate("3.3#")
    num = calculate(lst)
    assert num == 6


def test_complicated_expression():
    # 1
    lst = validate("8+---((---3*2)-(2^2)-5)-5*((8-2)+3)")
    num = calculate(lst)
    assert num == -22

    # 2
    lst = validate("        --3$5!-30*(5+8)+(((2^0-1)))")
    num = calculate(lst)
    assert num == -270

    # 3
    lst = validate("123.3#!     -- (--2^2)+3*8/2")
    num = calculate(lst)
    assert num == 362896

    # 4
    lst = validate("~---12!#--(22---2*3)")
    num = calculate(lst)
    assert num == 43

    # 5
    lst = validate("10@5#!#-50%(80---40)")
    num = calculate(lst)
    assert num == -3.5

    # 6
    lst = validate("(8/2/2/2---1)$39@40%3")
    num = calculate(lst)
    assert num == 0.5

    # 7
    lst = validate("(3^3%20---49)-((2.2#-2)-1)")
    num = calculate(lst)
    assert num == -23

    # 8
    lst = validate("~8&~1-9*2*3+52/20")
    num = calculate(lst)
    assert num == -59.4

    # 9
    lst = validate("(-~3)---(--~5/5)+8^2.5")
    num = calculate(lst)
    assert round(num) == 185

    # 10
    lst = validate("(11.11#-10.10#)!#-(68%5)")
    num = calculate(lst)
    assert num == -1

    # 11
    lst = validate("((5!-2!)#-(4!-2!)#)/2")
    num = calculate(lst)
    assert num == 3

    # 12
    lst = validate("90@-90---53+20%1*2*4")
    num = calculate(lst)
    assert num == -53

    # 13
    lst = validate("(28$29-(30&7)/2)-56.2")
    num = calculate(lst)
    assert round(num) == -31

    # 14
    lst = validate("(--8-~5)-14*-1+2.1+2.9")
    num = calculate(lst)
    assert num == 32

    # 15
    lst = validate("36.5/0.5-20^3+100%6.6")
    num = calculate(lst)
    assert num == -7926

    # 16
    lst = validate("(((---9--9)$86@2)/50)*0.2")
    num = calculate(lst)
    assert num == 0.17600000000000002

    # 17
    lst = validate("(5!#!#---23-24.8)%4")
    num = calculate(lst)
    assert num == 2.200000000000003

    # 18
    lst = validate("---~((---1&--0)*67/60)")
    num = calculate(lst)
    assert num == -1.1166666666666667

