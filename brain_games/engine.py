import prompt


def welcome_user():
    """Greets user, asks his name and returns it"""
    print('Welcome to the Brain Games!')
    NAME = prompt.string('May I have your name? ')
    print(f'Hello, {NAME}!')
    return NAME


def game(task, first, second, third):
    """Greets user, gives task, accepts answer, compares answer with correct answer. """
    NAME = welcome_user()

    print(task)       
    for tup in (first, second, third):
        expression, correct_answer = tup

        print('Question:', expression)
        answer = input('Your answer: ')

        if answer == correct_answer:
            print('Correct!')            
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {NAME}!")
            break

    else:
        print(f'Congratulations, {NAME}!')
