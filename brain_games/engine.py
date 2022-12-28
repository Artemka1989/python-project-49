from brain_games import cli
import prompt


WIN = 3


def logic(game):
    name = cli.welcome_user()
    print(game.GAME)
    score = 0
    while score != WIN:
        question, calc = game.play()
        print(question)
        answer = prompt.string("Your answer: ")
        if answer == str(calc):
            print("Correct!")
            score += 1
        else:
            cli.wrong(answer, name, calc)
            score -= 1
            break
    if score == 3:
        cli.correct(name)
