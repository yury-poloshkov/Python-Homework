# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

def GenerateRandomIntList():
    import random 
    n = int(input("Введите размер массива: "))
    min_number = int(input("Введите минимальное значение элемента массива: "))
    max_number = int(input("Введите максимальное значение элемента массива: "))
    numbers = []
    for i in range(n):
        numbers.append(random.randint(min_number,max_number))
    return numbers

list_1 = GenerateRandomIntList()
print(list_1)
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
size= len(list_1)

x_min = int(input("Введите отслеживаемый минимум: "))
x_max = int(input("Введите отслеживаемый максимум: "))

found_indexes = list()
for i in range(size):
    if x_max >= list_1[i] >= x_min:
        found_indexes.append(i)
print(found_indexes)