#ПОИСК
#Контекст
#Предположим, что нам хочется для любого массива чисел array и любого числа target узнать содержится
#ли target в array. Такую процедуру будем называть поиском.
#Задача
#Реализовать императивную функцию поиска элементов на языке Python.

# Декларативный стиль
lis = list(range(10, 20))

target = 5
print(target in lis)

target = 15
print(target in lis)

# Императивный стиль
lis = list(range(10, 20))

target = 55
for i in lis:
    if target == i:
        print(True)
        break
else:
    print(False)
