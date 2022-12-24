from random import randint


def task():
    return 'Find the greatest common divisor of given numbers.'


def result():
    """Returns tuple that contains two random numbers and the greatest common divisor of these numbers"""

    a, b = randint(0, 10), randint(0, 10)
    end = abs((a, b)[abs(a) < abs(b)])

    for num in range(end, 0, -1):
        if a % num == 0 and b % num == 0:

            return f'{a} {b}', str(num)


