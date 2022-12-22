import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    return name


def correct(name):
    print(f"Congratulations, {name}!")


def wrong(answer, name, calc):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{calc}'.")
    print(f"Let's try again, {name}!")
