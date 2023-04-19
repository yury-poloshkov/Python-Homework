# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

def GenerateRandomIntList():
    import random 
    n = int(input("Введите количество кустов: "))
    min_number = int(input("Введите минимальное количество ягод на кусте: "))
    max_number = int(input("Введите максимальное количество ягод на кусте: "))
    numbers = []
    for i in range(n):
        numbers.append(random.randint(min_number,max_number))
    return numbers

garden = GenerateRandomIntList()
print(garden)

best_point = 0
best_point_sum = cur_point_sum = garden[-1] + garden[0] + garden[1]

print(best_point_sum)
for cur_point in range(1, len(garden)):
    cur_point_sum = cur_point_sum - garden[cur_point-2] + garden[(cur_point+1)%len(garden)]
    if best_point_sum < cur_point_sum:
        best_point = cur_point
        best_point_sum = cur_point_sum
print(str(best_point+1) + " : " + str(best_point_sum))