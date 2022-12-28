import random


GAME = 'What is the result of the expression?'
MAX_NUM = 10  # максимальное значение числа 1
MAX_NUM_1 = 10  # максимльное значение числа 2


def play():
    num = random.randint(0, MAX_NUM)
    operator = random.choice('+-*')
    num_1 = random.randint(0, MAX_NUM_1)
    question = f'Question: {num} {operator} {num_1}'
    if operator == '+':
        calc = num + num_1
    if operator == '-':
        calc = num - num_1
    if operator == '*':
        calc = num * num_1
    return question, calc
