#! usr/bin/env/python3
import prompt
from brain_games import cli
import random


def games():
    name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(1, 4):
        num = random.randint(1, 100)
        print(f'Question: {num}')
        answer = prompt.string("Your answer: ")
        question = even(num)
        if question == answer:
            print("Correct!")
        else:
            cli.wrong(answer, name, question)
            i -= 1
            break
    if i == 3:
        cli.correct(name)


def even(num):
    if num % 2 == 0:
        return "yes"
    else:
        return "no"
