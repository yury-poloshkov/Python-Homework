# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def calculate_progression(a_0, d, n):
    progression = list()
    for i in range(n):
        progression.append(a_0 + i*d)
    return progression

a_0 = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разность прогрессии: "))
n = int(input("Введите количество элементов прогрессии: "))
ar_progr = calculate_progression(a_0, d, n)
print(ar_progr)