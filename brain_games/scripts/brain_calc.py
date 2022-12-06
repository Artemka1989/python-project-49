#! usr/bin/env/ python3

import prompt
import random


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print("What is the result of the expression?")
    for i in range(1, 4):
        num = random.randint(0, 100)
        num_1 = random.randint(0, 100)
        operator = random.choice('+-*')
        print(f"Question: {num} {operator} {num_1}")
        answer = prompt.string("Your answer: ")
        q = calc(num, operator, num_1)
        if str(answer) == str(q):
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{q}'.")
            print(f"Let's try again, {name}!")
            break
        if i == 3:
            print(f"Congratulations, {name}!")


def calc(num, operator, num_1):
    if operator == "+":
        calc = num + num_1
    if operator == "-":
        calc = num - num_1
    if operator == "*":
        calc = num * num_1
    return calc


if __name__ == "__main__":
    main()
