# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

s = int(1)
while s % 6 != 0:
    s = int(input("Введите суммарное количество журавликов: "))
else:
    sPeter = int(s/6)
    print(f"Из {s} журавликов Петя сделал - {sPeter}, Катя - {sPeter*2*2}, Сережа - {sPeter}")