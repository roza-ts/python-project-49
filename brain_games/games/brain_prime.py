from random import randint


def task():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def result():
    """Returns tuple that contains random number and word "yes" if it's prime and word "not" if it's not"""  # noqa

    number = randint(1, 100)
    return number, 'yes' if is_prime(number) else 'no'


def is_prime(number):
    """Reports if number is prime"""

    if number == 1:
        return False
    for num in range(2, number):
        if number % num == 0:
            return False
    return True
