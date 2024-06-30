from random import randint


def task():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game(): 
    num = randint(0, 11)
    return num, ('no', 'yes')[is_prime(num)]


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
