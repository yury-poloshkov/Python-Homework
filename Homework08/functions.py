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

def search(file_name, searchMask = " ") :
    phoneBook = read_phoneBook(file_name)
    if searchMask != " ":
        phoneBook = list(filter(lambda x: searchMask.lower() in x.lower(), phoneBook))
    return phoneBook

def delete_contact(file_name, contact):
    phoneBook = read_phoneBook(file_name)
    phoneBook.remove(contact)
    data = open(file_name, 'w')
    data.writelines("%s\n" % contact for contact in phoneBook)
    data.close

def read_phoneBook(file_name):
    data = open(file_name, 'r')
    phoneBook = list()
    for line in data:
        phoneBook.append(line[:-1])
    data.close()
    return sorted(phoneBook)