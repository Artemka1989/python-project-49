#! usr/bin/env/ python3

import prompt
import random
from brain_games import cli


def main():
    user = cli.welcome_user()
    print('Answer "yes" if the number is prime. Otherwise answer "no".')
    for i in range(1, 4):
        num = random.randint(1, 100)
        print(f"Question: {num}")
        answer = prompt.string("Your answer: ")
        q = prime(num)
        if str(answer) == str(q):
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{q}'.")
            print(f"Let's try again, {user}!")
            i -= 1
            break
    if i == 3:
        print(f"Congratulations, {user}!")


def prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count <= 2:
        return "yes"
    else:
        return "no"


if __name__ == "__main__":
    main()
