# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':

    def get_list_of_all_files_name():
        list_of_all_files_name = (os.listdir(os.path.join(current_dir, migrations)))
        list_of_sql_files_name = []
        for file_name in list_of_all_files_name:
            file_extension = os.path.splitext(os.path.join(current_dir, file_name))
            if file_extension[1] == '.sql':
                list_of_sql_files_name.append(file_name)
        return list_of_sql_files_name

    def get_list_of_files_with_search_text(list_of_files_name, search_text):
        list_of_files_with_search_text = []
        for file_name in list_of_files_name:
            with open(os.path.join(current_dir, migrations, file_name)) as f:
                if search_text in f.read():
                    list_of_files_with_search_text.append(file_name)
        return list_of_files_with_search_text

    def print_information_about_files_with_search_text(list_for_print):
        if len(list_for_print) > 2:
            print('... большой список файлов ...')
        else:
            for file_name in list_for_print:
                print('{}/{}'.format(migrations, file_name))

        print('Всего: {}'.format(len(list_for_print)))

    list_of_files_with_search_text = []
    while True:
        if len(list_of_files_with_search_text) == 0:
            list_for_search = get_list_of_all_files_name()
        else:
            list_for_search = list_of_files_with_search_text
        search_text = input('Введите строку:')
        list_of_files_with_search_text = get_list_of_files_with_search_text(list_for_search, search_text)
        print_information_about_files_with_search_text(list_of_files_with_search_text)
    pass