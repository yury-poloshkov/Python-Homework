# Задача 26:  Посчитать факториал (произведение 1 до N) 
# и треугольное число (сумма чисел от 1 до N) для числа N
# ЧЕРЕЗ РЕКУРСИЮ и без циклов

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

def triangle(n):
    if n <= 1:
        return 1
    return n + triangle(n-1) 

number = int(input("Введите число: "))
f_number = factorial(number)
t_number = triangle(number)
print(f"{number}! = {f_number}, Т{number} = {t_number}")

