def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phon.txt')
    phone_book2 = read_txt('phon2.txt')

    while choice != 7:
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('Введите фамилию: ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            number = input('Введите номер: ')
            print(find_by_number(phone_book, number))
        elif choice == 4:
            user_data = input('Введите новые данные через запятую без пробелов: ')
            add_user(phone_book, user_data)
            write_txt('phon.txt', phone_book)
            
        elif choice == 5:
            last_name = input('Введите фамилию: ')
            new_number = input('Введите новый номер: ')
            print(change_number(phone_book, last_name, new_number))
        elif choice == 6:
            write_txt('phon.txt', phone_book)
        elif choice == 8:
            n = input('Введите id абонента: ')
            write_in_another_file(phone_book, phone_book2, n)
            write_txt('phon2.txt', phone_book2)

        choice = show_menu()

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Изменить данные абонента\n"
          "6. Сохранить справочник в текстовом формате\n"
          "7. Закончить работу\n"
          "8. Копирование в другой файл")
    choice = int(input())
    return choice

def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    i = 1

    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.strip().split(',')))
            record['id'] = str(i)
            i += 1
            phone_book.append(record)

    return phone_book

def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        # for record in phone_book:
        #     s = ','.join(record.values())
        #     phout.write(f'{s}\n')
        for record in phone_book:
            line = f"{record['Фамилия']},{record['Имя']},{record['Телефон']},{record['Описание']},{record['id']}"
            phout.write(f'{line}\n')

# Функции, которые необходимо добавить:
def print_result(phone_book):
    for record in phone_book:
        print(record)

def find_by_lastname(phone_book, last_name):
    results = [record for record in phone_book if record['Фамилия'] == last_name]
    return results if results else 'Абонент не найден'

def change_number(phone_book, last_name, new_number):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            record['Телефон'] = new_number
            return 'Номер изменён'
    return 'Абонент не найден'

def delete_by_lastname(phone_book, lastname):
    initial_length = len(phone_book)
    phone_book[:] = [record for record in phone_book if record['Фамилия'] != lastname]
    return 'Абонент удалён' if len(phone_book) < initial_length else 'Абонент не найден'

def find_by_number(phone_book, number):
    results = [record for record in phone_book if record['Телефон'] == number]
    return results if results else 'Номер не найден'

def add_user(phone_book, user_data):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    values = user_data.split(',')
    if len(values) == len(fields):
        record = (dict(zip(fields, values)))
        record['id'] = str(len(phone_book) + 1)
        phone_book.append(record)
        return 'Абонент добавлен'
    return 'Некорректные данные'

def write_in_another_file(phone_book, phone_book2, n):
    search_id = next((record for record in phone_book if record['id'] == n), None)
    phone_book2.append(search_id)

work_with_phonebook()

