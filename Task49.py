
import csv

def work_with_phonebook():
    phone_book = read_csv('phonebook.csv')
    while True:
        choice = show_menu()
        if choice==7:
            break
        elif choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('Введите фамилию: ')
            result = find_by_lastname(phone_book,last_name)
            if len(result) == 0:
                print("Такого клиента нет")
            else:
                print_result(result)
        elif choice==3:
            last_name=input('Введите фамилию: ')
            result = find_by_lastname(phone_book,last_name)
            if len(result) == 0:
                print("Такого клиента нет")
            else:
                new_number=input('Введите новый номер: ')
                change_number(phone_book,last_name,new_number)
                write_csv('phonebook.csv',phone_book)
        elif choice==4: 
            last_name=input('Введите фамилию: ')
            result = find_by_lastname(phone_book, last_name)
            if len(result) == 0:
                print("Такого клиента нет")
            else:
                delete_by_lastname(phone_book,last_name)
                write_csv('phonebook.csv',phone_book)
        elif choice==5:
            number=input('Введите номер: ')
            result = find_by_number(phone_book,number)
            if len(result) == 0:
                print("Такого клиента нет")
            else:
                print_result(result)
        elif choice==6:
            user_data=input('Введите новые данные в формате "фамилия,имя,номер,описание": ')
            add_user(phone_book,user_data)
            write_csv('phonebook.csv',phone_book)
                
def show_menu():
    print("\n1: Показать все записи\n2: Найти по фамилии\n3: Изменить номер\n4: Удалить запись\n5: Найти по номеру\n6: Добавить запись\n7: Выход")
    choice = int(input("Выберите команду: "))
    return choice

def print_result(phone_book):
    for person in phone_book:
        print(f"{person['Фамилия']},{person['Имя']},{person['Номер']},{person['Описание']}")

def find_by_lastname(phone_book, last_name):
    result = [person for person in phone_book if person['Фамилия'] == last_name]
    return result

def change_number(phone_book, last_name, new_number):
    for person in phone_book:
        if person['Фамилия'] == last_name:
            person['Номер'] = new_number

def delete_by_lastname(phone_book, last_name):
    phone_book[:] = [person for person in phone_book if person['Фамилия'] != last_name]

def find_by_number(phone_book, number):
    result = [person for person in phone_book if person['Номер'] == number]
    return result

def add_user(phone_book, user_data):
    fields = ['Фамилия', 'Имя', 'Номер', 'Описание']
    user_data_dict = dict(zip(fields, user_data.split(',')))
    phone_book.append(user_data_dict)

def read_csv(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Номер', 'Описание']
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, (item.strip() for item in line.strip().split(','))))
            phone_book.append(record) 
    return phone_book

def write_csv(filename, phone_book):
    fields = ['Фамилия', 'Имя', 'Номер', 'Описание']
    with open(filename, 'w', encoding='utf-8', newline='') as phb:
        writer = csv.DictWriter(phb, fieldnames=fields) 
        writer.writerows(phone_book)

work_with_phonebook()

