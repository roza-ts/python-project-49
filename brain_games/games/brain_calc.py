import operator
from random import randint, choice


def question():
    return 'What is the result of the expression?'


def result():
    """Returns tuple that contains random expression and result of it"""
    a, b = randint(0, 10), randint(0, 10)
    opr = choice(('+', '-', '*'))
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    return f'{a} {opr} {b}', str(operators[opr](a, b))


