
""" OpenWeatherMap (экспорт)

Сделать скрипт, экспортирующий данные из базы данных погоды, 
созданной скриптом openweather.py. Экспорт происходит в формате CSV или JSON.

Скрипт запускается из командной строки и получает на входе:
    export_openweather.py --csv filename [<город>]
    export_openweather.py --json filename [<город>]
    export_openweather.py --html filename [<город>]
    
При выгрузке в html можно по коду погоды (weather.id) подтянуть 
соответствующие картинки отсюда:  http://openweathermap.org/weather-conditions

Экспорт происходит в файл filename.

Опционально можно задать в командной строке город. В этом случае 
экспортируются только данные по указанному городу. Если города нет в базе -
выводится соответствующее сообщение.

"""

import csv
import json
import sys
import sqlite3


db_weather = 'weather.db'
csv.register_dialect('excel-semicolon', delimiter=';')
#encoding = 'utf-8'
encoding = 'windows-1251'


def open_db():
    with sqlite3.connect(db_weather) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Погода")
        column_names = [description[0] for description in cur.description]
        table_content = cur.fetchall()
    content = []
    for _ in range(len(table_content)):
        content.append(dict(zip(column_names, table_content[_])))
    return content, column_names


def export_json(fname, c_name=None):
    content, column_names = open_db()
    fname = fname + '.json'
    write_content = []
    if c_name:
        for elem in content:
            if c_name in elem.values():
                write_content.append(elem)
    else:
        write_content = content
    if len(write_content) == 0:
        print('Данных нет в базе')
        exit()
    with open(fname, 'w', encoding='UTF8') as write_json:
        json.dump(write_content, write_json, ensure_ascii=False, indent=2)


def export_csv(fname, c_name=None):
    content, column_names = open_db()
    fname = fname + '.csv'
    write_content = []
    if c_name:
        for elem in content:
            if c_name in elem.values():
                write_content.append(elem)
    else:
        write_content = content
    if len(write_content) == 0:
        print('Данных нет в базе')
        exit()
    with open(fname, 'w', encoding=encoding) as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=column_names, dialect='excel-semicolon')
        headers = {name: name for name in column_names}
        writer.writerow(headers)
        for _ in range(len(write_content)):
            writer.writerow(write_content[_])


do = {
    '--csv': export_csv,
    '--json': export_json,
}

try:
    city_name = sys.argv[3]
except IndexError:
    city_name = None

try:
    filename = sys.argv[2]
except IndexError:
    filename = None

try:
    operation = sys.argv[1]
except IndexError:
    operation = None

if operation:
    if do[operation]:
        do[operation](filename, city_name)
    else:
        print("Задана неверная команда")