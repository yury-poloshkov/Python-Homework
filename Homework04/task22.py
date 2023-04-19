# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.

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
list_2 = GenerateRandomIntList()
print(list_2)
print(sorted(set(list_1).intersection(set(list_2))))