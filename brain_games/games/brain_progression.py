from random import choice
      

def task():
    return 'What number is missing in the progression?'


def game(): 
    num1 = choice(range(1, 21))   
    return get_question_and_answer(get_progression(num1))


def get_progression(start):
    length, step = choice(range(5, 11)), choice(range(1, 5))
    return list(range(start, start + step * length, step))


def get_question_and_answer(seq):
    my_list = list(seq)
    chosen_index = choice(range(0, len(my_list) - 1))
    hidden_num = my_list[chosen_index]
    my_list[chosen_index] = '..'
    return ' '.join(map(str, my_list)), str(hidden_num)
