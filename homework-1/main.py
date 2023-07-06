"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2

#  Открываем файл и достаем информацию
with open('./north_data/employees_data.csv') as f:
    list_from_employees_data = []
    data = csv.reader(f, delimiter=",")
    for line in data:
        change_list_to_tuple = tuple(line)
        list_from_employees_data.append(change_list_to_tuple)
# Открываем файл и достаем информацию
with open('./north_data/customers_data.csv') as f:
    list_from_customers_data = []
    data = csv.reader(f, delimiter=",")
    for line in data:
        change_list_to_tuple = tuple(line)
        list_from_customers_data.append(change_list_to_tuple)
# Открываем файл и достаем информацию
with open('./north_data/orders_data.csv') as f:
    list_from_orders_data = []
    data = csv.reader(f, delimiter=",")
    for line in data:
        change_list_to_tuple = tuple(line)
        list_from_orders_data.append(change_list_to_tuple)

# Подключаемся к базе данных
conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='')  # Данные БД
cur = conn.cursor()  # Включение курсора
cur.executemany('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', list_from_employees_data[1:])  # Добавление списка кортежей в таблицы
cur.executemany('INSERT INTO customers VALUES (%s, %s, %s)', list_from_customers_data[1:])  # Добавление списка кортежей в таблицы
cur.executemany('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', list_from_orders_data[1:])  # Добавление списка кортежей в таблицы
conn.commit()  # запушить(закомитить) измененния на локальном сервере

cur.close()  # Закрываем курсор
conn.close()  # Закрываем подключение к БД