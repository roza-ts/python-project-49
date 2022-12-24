import random


def task():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def result():
    """Returns tuple that contains random number and word 'yes' if it's even, word 'no' if it's not'"""
    number = random.randint(-100, 100)
    return number, 'yes' if int(number) % 2 == 0 else 'no'
