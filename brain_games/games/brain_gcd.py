#!/usr/bin/env python3
import prompt
import random
from brain_games import cli


def games():
    name = cli.welcome_user()
    print("Find the greatest common divisor of given numbers.")
    for i in range(1, 4):
        num = random.randint(1, 100)
        num_1 = random.randint(1, 100)
        print(f"Question: {num} {num_1}")
        answer = prompt.string("Your answer: ")
        question = gcd_loop(num, num_1)
        if str(question) == str(answer):
            print("Correct!")
        else:
            cli.wrong(answer, name, question)
            i -= 1
            break
    if i == 3:
        cli.correct(name)


def gcd_loop(num, num_1):
    if num > num_1:
        temp = num_1
    else:
        temp = num
    for i in range(1, temp + 1):
        if ((num % i == 0) and (num_1 % i == 0)):
            gcd = i
    return gcd
