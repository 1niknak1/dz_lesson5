import csv
import json

from files import CSV_FILE_PATH, JSON_FILE_PATH

# Открыть json-файл, записать его содержимое в список.
with open(JSON_FILE_PATH) as f:
    users_list = json.load(f)

# Создать новый список new_users_list со структурой, как у образца reference.json
new_users_list = []
for user in users_list:
    new_user_dict = {
        "name": user['name'],
        "gender": user['gender'],
        "address": user['address'],
        "age": user['age'],
        "books": []
    }
    new_users_list.append(new_user_dict)

# Создать новый список new_books_list со структурой, как у элементов массива books в образце reference.json
new_books_list = []
with open(CSV_FILE_PATH) as f:
    rd = csv.DictReader(f)
    for row in rd:
        new_book_dict = {
            "title": row['Title'],
            "author": row['Author'],
            "pages": int(row['Pages']),
            "genre": row['Genre']
        }
        new_books_list.append(new_book_dict)

# Отдать верхнюю книгу пользователю
user_counter = 0                                # Счетчик пользователей
while len(new_books_list) != 0:                 # Пока не кончились книги
    if user_counter == len(new_users_list):     # Ставим пользователей в хоровод, если пользователи закончились,
        user_counter = 0                        # то начинаем сначала
    else:
        book_in_this_iteration = new_books_list.pop(0)   # Взять верхнюю книгу (удаляя ее из списка)
        new_users_list[user_counter]['books'].append(book_in_this_iteration)  # Прибавить книгу в массив книг юзера
        user_counter += 1                                # Позвать следующего пользователя из хоровода


# Записать список пользователей в json файл
with open('../hw/users_with_books.json', 'w') as f:
    s = json.dump(new_users_list, f, indent=4)
    f.write(s)
