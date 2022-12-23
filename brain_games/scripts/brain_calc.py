import random
import prompt
import operator


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('What is the result of the expression?')

    for _ in range(3):
        operators = {'+': operator.add, '-': operator.sub, '*': operator.mul}
        a, b = random.randint(0, 10), random.randint(0, 10)
        op = random.choice(('+', '-', '*'))

        print('Question:', f'{a} {op} {b}')
        answer = int(input('Your answer: '))
        correct_answer = operators[op](a, b)

        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()

