import random


GAME = 'What is the result of the expression?'
MAX_NUM = 10  # максимальное значение числа


def play():
    num1 = random.randint(0, MAX_NUM)
    operator = random.choice('+-*')
    num2 = random.randint(0, MAX_NUM)
    question = f'{num1} {operator} {num2}'
    return question, calc(num1, num2, operator)


def calc(num1, num2, operator):
    if operator == '+':
        calc = num1 + num2
    if operator == '-':
        calc = num1 - num2
    if operator == '*':
        calc = num1 * num2
    return calc
