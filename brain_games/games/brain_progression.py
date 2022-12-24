from random import randrange


def task():
    return 'What number is missing in the progression?'


def result():
    """Returns tuple that contains progression with missing number and this number"""  # noqa

    start = randrange(51)
    step = randrange(1, 6)
    end = start + step * 10
    progression = list(range(start, end, step))

    index = randrange(len(progression))
    number = progression.pop(index)
    progression.insert(index, '..')
    string_progression = ' '.join(str(num) for num in progression)

# number = progression[index]
# progression[index] = '..'

    return f'{string_progression}', str(number)
