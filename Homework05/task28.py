# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
# 4 

def sum(a,b):
    if b == 0:
        if a == 0:
            return 0
        return sum(a-1,0) + 1
    return sum(a, b-1) + 1

a = int(input("Введите 1-е слагаемое: "))
b = int(input("Введите 2-е слагаемое: "))
summa = sum(a,b)
print(f"{a} + {b} = {summa}")