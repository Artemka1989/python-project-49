import random

GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MAX_NUM = 100  # Максимальное значение числа


def play():
    num = random.randint(0, MAX_NUM)
    question = f'{num}'
    if is_even(num):
        calc = 'yes'
    else:
        calc = 'no'
    return question, calc


def is_even(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count <= 2:
        return True
    else:
        return False
