import random

GAME = 'What number is missing in the progression?'
MIN_NUM = 2  # Минимальное значение первого числа прогрессии
MAX_NUM = 10  # Максимльное значение первого числа прогрессии
MIN_RANGE = 6  # Минимальное значение длины прогрессии
MAX_RANGE = 11  # Максимальное значение длины прогрессии
MIN_HIDDEN_NUM = 1  # Минимальное значение,где будет спрятано число
MAX_HIDDEN_NUM = 5  # Максимльное значение, где будет спрятано число


def play():
    num = random.randint(MIN_NUM, MAX_NUM)
    diaposon = num - 1  # Диапазон увеличение прогрессии
    range_ = random.randint(MIN_RANGE, MAX_RANGE)
    hidden_num = random.randint(MIN_HIDDEN_NUM, MAX_HIDDEN_NUM)
    return progression(num, diaposon, range_, hidden_num)


def progression(num, diaposon, range_, hidden_num):
    progression = []
    for i in range(1, range_):
        if i == hidden_num:
            progression.append('..')
            calc = num
            num += range_
        progression.append(str(num))
        num += range_
    string = ' '.join(progression)
    question = f'{string}'
    return question, calc
