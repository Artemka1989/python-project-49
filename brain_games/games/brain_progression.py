#!/usr/bin/env python3
import random

game = "What number is missing in the progression?"


def games():
    num = random.randint(2, 10)
    num_1 = num - 1
    ran = random.randint(6, 11)
    num_2 = random.randint(1, 5)
    lst = []
    for i in range(1, ran):
        if i == num_2:
            lst.append("..")
            calc = num
            num += num_1
        lst.append(str(num))
        num += num_1
    string = " ".join(lst)
    question = f'Question: {string}'
    return question, calc
