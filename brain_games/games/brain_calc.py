from random import sample, choice
from operator import add, sub, mul
        

def task():
    return 'What is the result of the expression?'


def game():
    symbols = {add: '+', sub: '-', mul: '*'}
    num1, num2 = sample(range(0, 10), 2)
    operator = choice((add, sub, mul)) 
    return f'{num1} {symbols[operator]} {num2}', str(operator(num1, num2))
