# Task 38:

# Seminar:
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Поиск по фамилии

# 1 - Интерфейс
# 2 - работа с файлом
# 3 - алгоритм

# 1 - добавление контакта
# 2 - вывод всех
# 3 - поиск по фамилии
# 4 - выход

# Homework:
# Дополнить телефонный справочник возможностью изменения и удаления данных.

from functions import create
from interface import *

path = "phone_book.txt"

create(path, initialContacts= ['Иванов Иван Иванович +79625684622',
                               'Петров Петр Петрович +14567823354',
                               'Андреев Андрей Андреевич +34567891245'])

userChoice = -1
while userChoice != 0:
    userChoice = ShowMainMenu()
    if userChoice == 1:
        CreateNewContact(path)
    elif userChoice == 2:
        ShowAllContacts(path)
        TimeOut()
    elif userChoice == 3:
        FindContact(path)
        TimeOut()
    elif userChoice == 4:
        ChangeContact(path)
    elif userChoice == 5:
        DeleteContact(path)
print("\nПриложение закрывается. Будем рады видеть Вас снова!\n")