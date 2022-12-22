#!/usr/bin/env python3
import random


game = 'Answer "yes" if the number is even, otherwise answer "no".'


def games():
    num = random.randint(1, 100)
    question = f'Question: {num}'
    if num % 2 == 0:
        calc = 'yes'
    else:
        calc = 'no'
    return question, calc
