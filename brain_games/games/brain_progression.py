import random

GAME = 'What number is missing in the progression?'
MIN_NUM = 2  # Minimum value of the first number of the progression
MAX_NUM = 10  # Maximum value of first number in progression
MIN_RANGE = 6  # Minimum length value of progression
MAX_RANGE = 11  # Maximum length value of progression
MIN_HIDDEN_NUM = 1  # Minimum value for hidden number
MAX_HIDDEN_NUM = 5  # Maximum value for hidden number


def play():
    num = random.randint(MIN_NUM, MAX_NUM)
    diaposon = num - 1  # Range of progression increase
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
