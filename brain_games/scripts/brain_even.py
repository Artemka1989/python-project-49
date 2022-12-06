#! usr/bin/env/ python3

import prompt
import random


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, Otherwise answer "no".')
    print(f"Congratulations, {name}!")
    for i in range(1, 4):
        num = random.randint(1, 100)
        print(f"Question: {num}")
        answer = prompt.string("Your answer: ")
        q = even(num)
        if str(answer) == str(q):
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{q}'.")
            print(f"Let's try again, {name}!")
            break
        if i == 3:
            print(f"Congratulations, {name}!")


def even(num):
    if num % 2 == 0:
        return "yes"
    else:
        return "no"


if __name__ == "__main__":
    main()
