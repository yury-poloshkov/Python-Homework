# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 3 2 3 7 5
# Ввод: 3
# -> 2 

import random 

n = int(input("Введите размер массива: "))
min_number = int(input("Введите минимальное значение элемента массива: "))
max_number = int(input("Введите максимальное значение элемента массива: "))
numbers = []
for i in range(n):
    numbers.append(random.randint(min_number,max_number))
print(numbers)

x = int(input("Введите искомое значение: "))
count_x = 0
for i in range(len(numbers)):
    if numbers[i] == x:
        count_x += 1
print(f"Количество элементов равных {x} - {count_x}")