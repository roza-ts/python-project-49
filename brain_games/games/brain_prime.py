import operator
from random import randint


def task():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def result():
    """Returns tuple that contains random number and word "yes" if it's prime and word "not" if it's not"""

    number = randint(-100, 100)
    return number, 'yes' if is_prime(number) else 'no'


def is_prime(number):
    """Reports if number is prime"""

    end = abs(number)
    for num in range(2, end):
        if number % num == 0:
            return False
    return True
