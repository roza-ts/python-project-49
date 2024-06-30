from random import choice


def task():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def game():
    num = choice(range(0, 1001))
    return num, ('no', 'yes')[is_even(num)]


def is_even(number):
    return number % 2 == 0
