#!/usr/bin/env python3
import random

game = "Find the greatest common divisor of given numbers."


def games():
    num = random.randint(1, 100)
    num_1 = random.randint(1, 100)
    question = f"Question: {num} {num_1}"
    if num > num_1:
        temp = num_1
    else:
        temp = num
    for i in range(1, temp + 1):
        if ((num % i == 0) and (num_1 % i == 0)):
            calc = i
    return question, calc
