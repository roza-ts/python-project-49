import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def is_even(num):
    return 'yes' if int(num) % 2 == 0 else 'no'


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        question = input('Question: ')
        answer = input('Your answer: ')
        if answer == is_even(question):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{is_even(question)}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
	main()
