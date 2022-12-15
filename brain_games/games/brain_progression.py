#! usr/bin/env/ python3

import random
import prompt
from brain_games import cli


def games():
    name = cli.welcome_user()
    count = 0
    for i in range(1, 100):
        num = random.randint(2, 10)
        num_1 = num - 1
        ran = random.randint(5, 11)
        num_2 = random.randint(1, 11)
        if count == 3:
            cli.correct(name)
            break
        if ran > num_2:
            string, question = progression(num, num_1, ran, num_2)
            print(f'Question: {string}')
            answer = prompt.string("Your answer: ")
            if str(question) == answer:
                print("Correct!")
                count += 1
            else:
                cli.wrong(answer, name, question)
                i -= 1
                break


def progression(num, num_1, ran, num_2):
    lst = []
    print("What number is missing in the progression?")
    for i in range(1, ran):
        if i == num_2:
            lst.append("..")
            question = num
            num += num_1
        lst.append(str(num))
        num += num_1
    return " ".join(lst), question
