import prompt


def action(what_game):
    name = welcome_user()
    print(what_game.task())

    for _ in range(3):
        fill, right_answer = what_game.game()
        our_answer = answer(fill)
        if our_answer == right_answer:
            print('Correct!')
        else:
            return f"""'{our_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.
Let's try again, {name}!""" # noqa

    return f'Congratulations, {name}!'


def welcome_user():
    print('Welcome to the Brain games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def answer(fill):
    return input(f'''Question: {fill}
Your answer: ''')
