#!/usr/bin/env python3
import prompt
from brain_games import cli
import random


def games():
    name = cli.welcome_user()
    print("What is the result of the expression?")
    for i in range(1, 4):
        num = random.randint(1, 10)
        num_1 = random.randint(1, 10)
        operator = random.choice('+-*')
        print(f"Question: {num} {operator} {num_1}")
        answer = prompt.string("Your answer: ")
        question = calc(num, operator, num_1)
        if answer == str(question):
            print("Correct!")
        else:
            cli.wrong(answer, name, question)
            i -= 1
            break
    if i == 3:
        cli.correct(name)


def calc(num, operator, num_1):
    if operator == "+":
        calc = num + num_1
    if operator == "-":
        calc = num - num_1
    if operator == "*":
        calc = num * num_1
    return calc
