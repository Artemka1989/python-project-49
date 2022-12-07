#! usr/bin/env/ python3

import prompt
import random
print("Welcome to the Brain Games!")


def main():
    i = 0
    name = prompt.string("May I have your name? ")
    print('Hello, ' + name + '!')
    print("Find the greatest common divisor of given numbers.")
    for i in range(1, 4):
        num = random.randint(1, 100)
        num_1 = random.randint(1, 100)
        print(f"Question: {num} {num_1}")
        answer = prompt.string("Your answer: ")
        q = gcd_loop(num, num_1)
        if str(q) == str(answer):
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{q}'")
            print(f"Let's try again, {name}!")
            break
    if i == 3:
        print(f"Congratulations, {name}!")


def gcd_loop(num, num_1):
    if num > num_1:
        temp = num_1
    else:
        temp = num
    for i in range(1, temp + 1):
        if ((num % i == 0) and (num_1 % i == 0)):
            gcd = i
    return gcd


if __name__ == "__main__":
    main()
