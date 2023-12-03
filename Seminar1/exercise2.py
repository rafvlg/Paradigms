#ДОЛЯ ЧИСЕЛ
#● Условие
#На вход подается: список целых чисел arr
#● Задача
#Реализовать императивную функцию, которая возвращает три числа:
#○ Долю позитивных чисел
#○ Долю нулей
#○ Долю отрицательных чисел

def metod(set_):
    total = len(set_)
    if not total:
        return 0, 0, 0

    pos = len([i for i in set_ if i > 0]) / total
    neg = len([i for i in set_ if i < 0]) / total
    zeros = len([i for i in set_ if i == 0]) / total

    return pos, neg, zeros

def metod2(set_):
    total = len(set_)

    pos = sum(map(lambda x: x > 0, set_)) / total
    neg = sum(map(lambda x: x < 0, set_)) / total
    zeros = sum(map(lambda x: x == 0, set_)) / total

    return pos, neg, zeros

stt_ = set(range(-10, 10))

m = metod(stt_)
m2 = metod2(stt_)

print(*m)

print(*m2)