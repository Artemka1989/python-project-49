from brain_games import cli
import prompt


def logic(game, games):
    name = cli.welcome_user()
    print(game)
    score = 0
    WIN = 3
    while score != WIN:
        question, calc = games()
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
