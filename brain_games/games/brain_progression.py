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
    num_1 = num - 1  # Диапазон увеличение прогрессии
    ran = random.randint(MIN_RANGE, MAX_RANGE)
    num_2 = random.randint(MIN_HIDDEN_NUM, MAX_HIDDEN_NUM)
    progression = []
    for i in range(1, ran):
        if i == num_2:
            progression.append('..')
            calc = num
            num += num_1
        progression.append(str(num))
        num += num_1
    string = ' '.join(progression)
    question = f'{string}'
    return question, calc
