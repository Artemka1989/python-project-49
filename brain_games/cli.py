import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    user = prompt.string("May I have your name? ")
    print(f'Hello, {user}!')
    return user
