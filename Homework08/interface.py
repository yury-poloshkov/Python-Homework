from functions import *

def ShowMainMenu():
    options= ("ТЕЛЕФОННЫЙ СПРАВОЧНИК v.2023.05.24", 
            "----- Главное меню -----",
            "1 - добавить контакт", 
            "2 - отобразить справочник", 
            "3 - найти контакт",
            "4 - изменить контакт",
            "5 - удалить контакт",
            "0 - выход")
    
    print()
    for option in options:
        print(option)

    userChoice = int(input("\nВведите код операции: "))
    return userChoice

def CreateNewContact(path):
    print("\n---- Введите данные контакта -----")
    familyName = input("Фамилия: ")
    firstName = input("Имя: ")
    secondName = input("Отчество: ")
    phoneNumber = input("Номер телефона: ")
    add_cont(path, familyName + " " + firstName + " " + secondName + " " + phoneNumber)

def ShowAllContacts(path):
    print("\n ----- Список имеющихся контактов -----")
    show_all(path)


def FindContact(path):
    searchMask = input("\nВведите данные для поиска: ")
    print("\n----- Результаты поиска -----")
    search(path, searchMask)

def ChangeContact(path):
    ShowAllContacts(path)
    idContact = int(input("\nВведите номер контакта для изменения: "))
    delete_contact(path, idContact)
    CreateNewContact(path)

def DeleteContact(path):
    ShowAllContacts(path)
    idContact = int(input("\nВведите номер контакта для удаления: "))
    delete_contact(path, idContact)

def TimeOut():
    input("\nДля продолжения работы нажмите Enter")