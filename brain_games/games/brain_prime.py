#! usr/bin/env/ python3
import prompt
import random
from brain_games import cli


def games():
    name = cli.welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(1, 4):
        num = random.randint(1, 100)
        print(f"Question: {num}")
        answer = prompt.string("Your answer: ")
        question = prime(num)
        if answer == question:
            print("Correct!")
        else:
            cli.wrong(answer, name, question)
            i -= 1
            break
    if i == 3:
        cli.correct(name)


def prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count <= 2:
        return "yes"
    else:
        return "no"
