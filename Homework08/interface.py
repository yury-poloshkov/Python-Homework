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
    phoneBook = read_phoneBook(path)
    PrintPhoneBook(phoneBook, "----- Список имеющихся контактов -----")


def FindContact(path):
    searchMask = input("\nВведите данные для поиска: ")
    phoneBook = search(path, searchMask)
    PrintPhoneBook(phoneBook, "----- Результаты поиска -----")
    return phoneBook

def ChangeContact(path):
    filtredPhoneBook = FindContact(path)
    if len(filtredPhoneBook) != 0:
        idContact = int(input("\nВведите номер контакта для изменения: "))
        delete_contact(path, filtredPhoneBook[idContact-1])
        CreateNewContact(path)

def DeleteContact(path):
    filtredPhoneBook = FindContact(path)
    if len(filtredPhoneBook) != 0:
        idContact = int(input("\nВведите номер контакта для удаления: "))
        delete_contact(path, filtredPhoneBook[idContact-1])

def TimeOut():
    input("\nДля продолжения работы нажмите Enter")

def PrintPhoneBook(array, header):
    print("\n" + header)
    if len(array) == 0:
        print("Список контактов пуст")
    else:
        for i in range(len(array)):
            print(str(i+1) + ". " +array[i])