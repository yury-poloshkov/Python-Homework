def create(path, initialContacts):
    try:
        file = open(path, 'r')
    except IOError:
        print('Создан новый справочник -> ' + path)
        file = open(path, 'w')
        file.writelines("%s\n" % contact for contact in initialContacts)
    finally:
        file.close()

def add_cont(file_name, newContact):
    data = open(file_name, 'a')
    data.write(newContact + "\n")
    data.close()

def show_all(file_name):
    data = open(file_name, "r")
    i = 1
    for line in data:
        print(str(i) + ". " + line[:-1])
        i += 1
    data.close()

def search(file_name, stroka = " ") :
    data = open(file_name, 'r')
    i = 0
    for line in data:
        if stroka.lower() in line.lower():
            i += 1
            print(str(i) + ". " + line[:-1])
    if i == 0:
        print("По заданным условиям поиска ничего не обнаружено")
    data.close()

def delete_contact(file_name, contact_id):
    data = open(file_name, 'r')
    phoneBook = list()
    for line in data:
        phoneBook.append(line[:-1])
    phoneBook.pop(contact_id - 1)
    data = open(file_name, 'w')
    data.writelines("%s\n" % contact for contact in phoneBook)
    data.close