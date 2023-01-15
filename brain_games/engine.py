import prompt


WIN = 3


def start(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME)
    score = 0
    while score < WIN:
        question, calc = game.play()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == str(calc):
            print('Correct!')
            score += 1
        else:
            print(f"'{answer}' is wrong answer ;(.", end=" ")
            print(f"Correct answer was '{calc}'.")
            print(f"Let's try again, {name}!")
            return
    if score == WIN:
        print(f"Congratulations, {name}!")
