import random

GAME = 'Find the greatest common divisor of given numbers.'
MAX_NUM = 100  # Максимальное значение первого числа
MAX_NUM_1 = 100  # Максимальное значение второго числа


def play():
    num = random.randint(0, MAX_NUM)
    num_1 = random.randint(0, MAX_NUM_1)
    question = f'Question: {num} {num_1}'
    if num > num_1:
        temp = num_1
    else:
        temp = num
    for i in range(1, temp + 1):
        if ((num % i == 0) and (num_1 % i == 0)):
            calc = i
    return question, calc
