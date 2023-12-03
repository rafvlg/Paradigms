#Таблица умножения
#● Условие
#На вход подается число n.
#● Задача
#Написать скрипт в любой парадигме, который выводит на экран
#таблицу умножения всех чисел от 1 до n.
#Обоснуйте выбор парадигм.
#● Пример вывода:
#1 * 1 = 1
#1 * 2 = 2
#1 * 3 = 3
#1 * 4 = 4
#1 * 5 = 5
#1 * 6 = 6
#..
#1 * 9 = 9

def multiplication_table(n):
    for i in range(1, n+1):
        for j in range(1, 10):
            print(f"{i} * {j} = {i*j}")

n = int(input("Введите число n: "))
multiplication_table(n)

#- Мы определяем функцию `multiplication_table`,
# которая принимает число `n` в качестве аргумента.
#- Внутри функции, мы используем два вложенных цикла:
# первый цикл перебирает числа от 1 до `n`,
# а второй цикл перебирает числа от 1 до 9
# (так как таблица умножения обычно состоит из умножений
# на числа от 1 до 9).
#- В каждой итерации циклов, мы выводим на экран уравнение
# умножения в нужном формате.