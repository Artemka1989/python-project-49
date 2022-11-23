#! usr/bin/env/ python3

import prompt
import random

print("Welcome to the brain-games!")


def main():
    i = 0
    name = prompt.string("May I have your name? ")
    print('Hello, ' + name + '!')
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    while i < 3:
        num = random.randint(0, 100)
        num_1 = random.randint(0, 100)
        operator = random.choice('+-*')
        print("Question: " + str(num) + " " + operator + " " + str(num_1))
        answer = prompt.string("Your answer: ")
        if operator == "+":
            calc = num + num_1
        if operator == "-":
            calc = num - num_1
        if operator == "*":
            calc = num * num_1
        if str(answer) == str(calc):
            print("Correct!")
        else:
            print(f"Let's try again {name} {str(answer)} is wrong answer ;(.Correct answer was {str(calc)}.")
            break
        i += 1
    if i == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
