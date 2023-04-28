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