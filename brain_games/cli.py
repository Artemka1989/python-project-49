#! usr/bin/env/python3
import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    return name


def correct(name):
    print(f"Congratulations, {name}!")


def wrong(answer, name, question):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{question}'.")
    print(f"Let's try again, {name}!")
