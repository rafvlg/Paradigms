#Написать программу на python в любой парадигме для
#бинарного поиска. На вход подаётся целочисленный массив и
#число. На выходе - индекс элемента или -1, в случае если искомого
#элемента нет в массиве.

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Пример использования
my_array = [1, 3, 5, 7, 9, 11, 13]
target_element = 7

result = binary_search(my_array, target_element)
print("Индекс искомого элемента:", result)