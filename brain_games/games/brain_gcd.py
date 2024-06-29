from random import sample
      

def task():
    return 'Find the greatest common divisor of given numbers.'


def game():    
    num1, num2 = sample(range(1, 100), 2)    
    return f'{num1} {num2}', str(get_greatest_common_divisor(num1, num2))


def get_greatest_common_divisor(number1, number2):
    smaller_num, larger_num = min(number1, number2), max(number1, number2)
    for i in range(smaller_num, 0, -1):        
        if larger_num % i == 0 and smaller_num % i == 0:
            return i
