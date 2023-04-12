# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input())

curResult = 1
while curResult <= n:
    print(curResult, end=" ")
    curResult *= 2
print()