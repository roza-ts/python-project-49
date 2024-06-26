import prompt
from random import choice


def game():
    name = welcome_user()
    print(game_even(name))

    
def game_even(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    for _ in range(3):
        num = choice(range(0, 1001))
        right_answer = ('no', 'yes')[is_even(num)]
        answer = input(f'''Question: {num}
Your answer: ''')
        if answer != right_answer:
            return f"""'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'.
Let's try again, {name}!"""
        else: 
            print('Correct!')
    return f'Congratulations, {name}!'
        



def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def is_even(number):
    return number % 2 == 0


