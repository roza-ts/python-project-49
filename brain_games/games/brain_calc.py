import operator
from random import randint, choice


def task():
    return 'What is the result of the expression?'


def result():
    """Returns tuple that contains random expression and value of it"""

    a, b = randint(0, 10), randint(0, 10)
    opr = choice(('+', '-', '*'))
    return f'{a} {opr} {b}', str(evaluate(a, b, opr))


def evaluate(a, b, opr):
    """Evaluates the value of the expression"""

    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    return operators[opr](a, b)
