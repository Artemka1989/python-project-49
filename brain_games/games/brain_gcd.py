import random
import math
GAME = 'Find the greatest common divisor of given numbers.'
MAX_NUM = 100  # Максимальное значение числа


def play():
    num = random.randint(1, MAX_NUM)
    num_1 = random.randint(1, MAX_NUM)
    question = f'{num} {num_1}'
    calc = math.gcd(num, num_1)
    return question, calc
