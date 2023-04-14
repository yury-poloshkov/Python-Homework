# Задача 18: Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 1 2 6 4 9
# Ввод: 8
# -> 9 

import random 

n = int(input("Введите размер массива: "))
min_number = int(input("Введите минимальное значение элемента массива: "))
max_number = int(input("Введите максимальное значение элемента массива: "))
numbers = []
for i in range(n):
    numbers.append(random.randint(min_number,max_number))
print(numbers)

x = int(input("Введите искомое значение: "))
x_nearest = numbers[0]
for i in  range(1, len(numbers)):
    if abs(x - numbers[i]) < abs(x - x_nearest):
        x_nearest = numbers[i]
print(f"Ближайшее к {x} - {x_nearest}")