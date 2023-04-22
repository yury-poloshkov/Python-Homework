# ** Дополнительно **
# 1. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

def fib(n):
    if n in [0, 1]:
        return n
    return fib(n-1) + fib(n-2)

number = int(input("Введите число: "))
fib_number = fib(number)
print(f"F{number} = {fib_number}")