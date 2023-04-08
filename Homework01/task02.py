# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(0)
while not(99 < number < 1000):
    number = int(input("Введите трехзначное число: "))
else:
    sumnumbers = 0
    numbercopy = number
    for i in range(3):
        sumnumbers += numbercopy % 10
        numbercopy //= 10
    print(f"Сумма цифр числа {number} равна {sumnumbers}")