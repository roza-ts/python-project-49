from random import randint


def task():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def result():
    """Returns tuple that contains random number and word "yes" if it's even and word "no" if it's not"""  # noqa

    number = randint(-100, 100)
    return number, 'yes' if is_even(number) else 'no'


def is_even(number):
    """Reports if number is even"""

    return int(number) % 2 == 0
