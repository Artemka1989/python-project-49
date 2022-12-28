import random

GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MAX_NUM = 100  # Максимальное значение числа


def play():
    num = random.randint(0, MAX_NUM)
    question = f'Question: {num}'
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count <= 2:
        calc = 'yes'
    else:
        calc = 'no'
    return question, calc
