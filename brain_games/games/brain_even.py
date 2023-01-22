import random


GAME = 'Answer "yes" if the number is even, otherwise answer "no".'
MAX_NUM = 100  # Максимальное число в игре


def play():
    num = random.randint(0, MAX_NUM)
    question = f'{num}'
    if is_even(num) is True:
        calc = 'yes'
    else:
        calc = 'no'
    return question, calc


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
