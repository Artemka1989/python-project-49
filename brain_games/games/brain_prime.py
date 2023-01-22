import random

GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MAX_NUM = 100  # Maximum value of number


def play():
    num = random.randint(0, MAX_NUM)
    question = f'{num}'
    if is_prime(num):
        calc = 'yes'
    else:
        calc = 'no'
    return question, calc


def is_prime(num):
    count = 0
    if num == 0 or num == 1:
        return False
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False
