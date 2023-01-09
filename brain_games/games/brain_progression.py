import random

GAME = 'What number is missing in the progression?'
MIN_NUM = 2  # Минимальное значение первого числа прогрессии
MAX_NUM = 10  # Максимльное значение первого числа прогрессии
MIN_RAN = 6  # Минимальное значение длины прогрессии
MAX_RAN = 11  # Максимальное значение длины прогрессии
MIN_NUM_1 = 1  # Минимальное значение,где будет спрятано число
MAX_NUM_1 = 5  # Максимльное значение, где будет спрятано число


def play():
    num = random.randint(MIN_NUM, MAX_NUM)
    num_1 = num - 1  # Диапазон увеличение прогрессии
    ran = random.randint(MIN_RAN, MAX_RAN)
    num_2 = random.randint(MIN_NUM_1, MAX_NUM_1)
    lst = []
    for i in range(1, ran):
        if i == num_2:
            lst.append('..')
            calc = num
            num += num_1
        lst.append(str(num))
        num += num_1
    string = ' '.join(lst)
    question = f'{string}'
    return question, calc
