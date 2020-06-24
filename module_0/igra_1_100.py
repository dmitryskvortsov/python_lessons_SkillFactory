import numpy as np


def game_core_v50(number):
    """Функция по угадыванию числа от 1 до 100 путем постоянного уменьшения диапазона значений
    в два раза, максимальное значение попыток - 7"""
    start = 0
    finish = 101
    count = 0
    predict = 0

    while True:
        predict = start + (finish - start) // 2
        count += 1

        if predict == number:
            break
        elif predict > number:
            finish = predict
        else:
            start = predict
    return count


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core_v50)
