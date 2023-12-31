#Корреляция
#● Контекст
#Корреляция - статистическая мера, используемая для оценки
#связи между двумя случайными величинами.
#● Ваша задача
#Написать скрипт для расчета корреляции Пирсона между
#двумя случайными величинами (двумя массивами). Можете
#использовать любую парадигму, но рекомендую использовать
#функциональную, т.к. в этом примере она значительно
#упростит вам жизнь.

from math import sqrt
from functools import reduce

def pearson_correlation(x, y):
    n = len(x)

    # Сумма элементов массива
    sum_x = sum(x)
    sum_y = sum(y)

    # Сумма квадратов элементов массива
    sum_x_squared = sum(map(lambda i: i*i, x))
    sum_y_squared = sum(map(lambda i: i*i, y))

    # Сумма произведений соответствующих элементов массивов
    sum_xy = sum(map(lambda i, j: i*j, x, y))

    # Расчет корреляции Пирсона
    numerator = (n * sum_xy) - (sum_x * sum_y)
    denominator = sqrt((n * sum_x_squared - sum_x**2) * (n * sum_y_squared - sum_y**2))

    if denominator == 0:
        return 0

    return numerator / denominator

# Пример использования
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

correlation = pearson_correlation(x, y)
print(f"Корреляция Пирсона: {correlation}")

#Объяснение:
#- Функция `pearson_correlation` принимает два массива `x`
# и `y` и вычисляет корреляцию Пирсона между ними.
#- Внутри функции, мы используем функцию `sum` для
# вычисления суммы элементов массива, функцию `map`
# для применения операций к каждому элементу массива,
# и функцию `reduce` для умножения и суммирования элементов.
#- Мы вычисляем все необходимые значения для формулы
# корреляции Пирсона и возвращаем результат.