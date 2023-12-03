#Задача №1
#Дан список целых чисел numbers.
#Необходимо написать в императивном стиле
#процедуру для сортировки числа в списке в порядке убывания.
#Можно использовать любой алгоритм сортировки.

def sort_list_imperative(numbers):
    # Используем алгоритм сортировки вставками
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] < key:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers

#Задание №2
#Написать точно такую же процедуру,
#но в декларативном стиле.

def sort_list_decrative(numbers):
    return sorted(numbers, reverse=True)
