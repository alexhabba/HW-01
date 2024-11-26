"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    return recursive_search(number, 1, 100)


# для решения этой задачи подходит рекурсивный алгоритм, сложность алгоритма логарифмическая
def recursive_search(num, start, end):
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число.
        start (int, optional): Начало диапазона.
        end (int, optional): Конец диапазона.

    Returns:
        int: Число попыток
    """
    count = 1
    # находим среднее значение интервала в котором ищем число
    mid = (start + end) // 2
    if (mid == num):
        return count
    elif num > mid:
        return count + recursive_search(num, mid + 1, end)
    else:
        return count + recursive_search(num, start, mid - 1)

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score

if __name__ == "__main__":
    # RUN
    score_game(random_predict)
