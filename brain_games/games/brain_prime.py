#!/usr/bin/env python3
import random


game = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def games():
    num = random.randint(1, 100)
    question = f"Question: {num}"
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count <= 2:
        calc = 'yes'
    else:
        calc = 'no'
    return question, calc
