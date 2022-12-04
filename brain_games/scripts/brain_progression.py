#! usr/bin/env python3

import random
import prompt
from brain_games import cli


def main():
    user = cli.welcome_user()
    i = 0
    while i != 3:
        num = random.randint(2, 10)
        num_1 = num - 1
        ran = random.randint(5, 11)
        num_2 = random.randint(1, 11)
        if ran > num_2:
            string, q = progression(num, num_1, ran, num_2)
            print(f'Question: {string}')
            a = prompt.string("Your answer: ")
            if str(q) == a:
                print("Correct!")
            else:
                print(f"'{a}' was a wrong answer ;(. Correct answer was '{q}'.")
                print(f"Let's try again {user} ")
                i -= 1
                break
        else:
            continue
        i += 1
    if i == 3:
        print(f"Congratulations, {user}!")


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


if __name__ == "__main__":
    main()
