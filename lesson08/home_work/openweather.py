"""
== OpenWeatherMap ==

OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.

Необходимо решить следующие задачи:

== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.

    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID,
    используя дополнительную библиотеку GRAB (pip install grab)

        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up

        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in

        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys

        Ключ имеет смысл сохранить в локальный файл, например, "app.id"


== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz

    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка
     (воспользоваться модулем gzip
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)

    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}


== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a

    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a

    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a


    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}


== Сохранение данных в локальную БД ==
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):

    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных

2. Выводить список стран из файла и предлагать пользователю выбрать страну
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))

3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.


При работе с XML-файлами:

Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с пространствами имен удобно пользоваться такими функциями:

    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    tree = ET.parse(f)
    root = tree.getroot()

    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}

    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...

"""

import json
import requests
import os
import sqlite3
from datetime import datetime

class Menu:
    __info = ('Вывести список стран',
              'Вывести список городов в стране',
              'Создать базу данных "weather.db"',
              'Загрузить погоду для одного города',
              'Загрузить погоду для нескольких городов',
              'Выйти из программы'
              )
    __info_answers = ('1', '2', '3', '4', '5', '6')

    def __init__(self):
        self.countries = Country()
        self.weather = Weather()

    def get_info(self):
        print('Данная программа реализует следующие функции:')
        for idx, elem in enumerate(self.__info):
            print(f'{idx + 1}. {elem}')

    def get_info_answer(self):
        while True:
            self.answer = input('Введите номер функции, которую хотите выполнить:\n')
            if self.answer in self.__info_answers:
                break
            else:
                print('Вы ввели неправильный номер, попробуйте еще раз!')
        if self.answer == '1':
            self.countries.get_country_list()
        elif self.answer == '2':
            self.countries.get_country_cities()
        elif self.answer == '3':
            self.weather.get_weather_db()
        elif self.answer == '4':
            self.weather.get_weather_one()
        elif self.answer == '5':
            self.weather.get_weather_group()
        elif self.answer == '6':
            exit()


class Country:
    def __init__(self):
        with open('city_list.json', 'rb') as read_list:
            self.all_countries = json.load(read_list)

    @property
    def __countries(self):
        country = set()
        self.__country_list = []
        for elem in self.all_countries:
            country.add(elem['country'])
        self.__country_list = list(country)
        self.__country_list.sort()
        self.__country_list = [i for i in self.__country_list if i.isalpha()]
        return self.__country_list

    def get_country_list(self):
        self.__country_list = self.__countries
        for idx, elem in enumerate(self.__country_list):
            print(f'{idx + 1}.{elem}'.ljust(6), end=' | ')
            if (idx + 1) % 10 == 0:
                print()
        print()

    def get_country_cities(self):
        self.__country_list = self.__countries
        city = set()
        __cities = []
        self.__cities_list = []
        while True:
            ans = input('Введите код страны для которой хотите получить список городов\n').upper()
            if ans in self.__country_list:
                break
            else:
                print('Вы ввели неправильный код страны, попробуйте еще раз!')
        for elem in self.all_countries:
            if elem['country'] == ans:
                city.add(elem['name'])
        self.__cities_list = list(city)
        self.__cities_list.sort()
        max_elem = max(list(map(len, self.__cities_list)))
        ans2 = input('Введите "ALL" если хотите вывести весь список, либо первую букву названия города на английчком:\n').upper()
        while True:
            if ans2 == 'ALL':
                for idx, elem in enumerate(self.__cities_list):
                    print(f'{idx + 1}.{elem}'.ljust(max_elem + 6), end=' | ')
                    if (idx + 1) % 3 == 0:
                        print()
                print()
                break
            elif len(ans2) == 1:
                for elem in self.__cities_list:
                    if elem and elem[0] == ans2:
                        __cities.append(elem)
                max_elem1 = max(list(map(len, __cities)))
                if len(__cities) != 0:
                    for idx, elem in enumerate(__cities):
                        print(f'{idx + 1}.{elem}'.ljust(max_elem1 + 5), end=' | ')
                        if (idx + 1) % 4 == 0:
                            print()
                    print()
                    break
                else:
                    print('Нет городов, начинающихся с такой буквы')
                    break
            else:
                print('Вы ввели неправильню команду')

    def city_id_one(self, city_name, country_name):
        id_of_one_city = ''
        for elem in self.all_countries:
            if city_name == elem['name'] and country_name == elem['country']:
                id_of_one_city = f'{elem["id"]}'
        return id_of_one_city

    def city_id_group(self, city_names, country_name):
        id_of_city = ''
        for elem in city_names:
            for city in self.all_countries:
                if elem == city['name'] and country_name == city['country']:
                    id_of_city += f'{city["id"]},'
        id_of_city = id_of_city[:-1]
        return id_of_city


class Weather:
    __api_url_one = 'http://api.openweathermap.org/data/2.5/weather'
    __api_url_group = 'http://api.openweathermap.org/data/2.5/group'
    __db_weather = 'weather.db'

    def __init__(self):
        with open('app.id', 'r') as read_app_id:
            self.__app_id = read_app_id.read().strip()
        self.data_city = Country()

    def get_weather_db(self):
        if self.__db_weather not in os.listdir('.'):
            with sqlite3.connect(self.__db_weather) as conn:
                conn.execute("""CREATE TABLE Погода(
                          id_города INTEGER PRIMARY KEY,
                          Город VARCHAR(255),
                          Дата DATE,
                          Температура INTEGER,
                          id_погоды INTEGER
                          )
                """)
            print('База данных "weather.db" успешно создана')
        else:
            print('База данных "weather.db" уже существует')

    def get_weather_one(self):
        ans_1 = input('Введите код страны для города которой хотите загрузить погоду:\n')
        ans_2 = input('Введите название города для которого хотите загрузить погоду:\n')
        __params = {
            'id': self.data_city.city_id_one(ans_2, ans_1),
            'appid': self.__app_id,
            'units': 'metric',
        }
        res = requests.get(self.__api_url_one, params=__params)
        one_city_data = res.json()
        write_one_city_data = [one_city_data['id'], one_city_data['name'],
                               datetime.utcfromtimestamp(one_city_data['dt']).strftime('%d-%m-%Y'),
                               one_city_data['main']['temp'], one_city_data['weather'][0]['id']
        ]
        self.get_weather_db()
        with sqlite3.connect(self.__db_weather) as conn:
            dt = []
            conn.execute("""INSERT OR IGNORE INTO Погода VALUES (?,?,?,?,?)""", write_one_city_data)

            ql = ("""UPDATE Погода 
                             SET Температура=?
                             WHERE id_города=? and Дата = ?"""
            )
            dt.append(write_one_city_data[3])
            dt.extend(write_one_city_data[1:3])
            cur = conn.cursor()
            cur.execute(ql, dt)
        print('Данные о погоде добавлены в базу "weather.db"')

    def get_weather_group(self):
        ans_2 = []
        write_group_city_data = []
        ans_1 = input('Введите код страны для городов которой хотите загрузить погоду:\n')
        ans_2.extend(input('Введите через запятую названия городов для которых хотите загрузить погоду:\n').title().split(','))
        __params = {
            'id': self.data_city.city_id_group(ans_2, ans_1),
            'appid': self.__app_id,
            'units': 'metric',
        }
        res = requests.get(self.__api_url_group, params=__params)
        group_city_data = res.json()
        for elem in group_city_data['list']:
            write_group_city_data.append([elem['id'], elem['name'],
                                          datetime.utcfromtimestamp(elem['dt']).strftime('%d-%m-%Y'),
                                          elem['main']['temp'], elem['weather'][0]['id']]
                                         )
        self.get_weather_db()
        with sqlite3.connect(self.__db_weather) as conn:
            for i in range(len(write_group_city_data)):
                dt = []
                conn.execute("""INSERT OR IGNORE INTO Погода VALUES (?,?,?,?,?)""", write_group_city_data[i])

                ql = ("""UPDATE Погода 
                                     SET Температура=?
                                     WHERE id_города=? and Дата = ?"""
                )
                dt.append(write_group_city_data[i][3])
                dt.extend(write_group_city_data[i][1:3])
                cur = conn.cursor()
                cur.execute(ql, dt)
        print('Данные о погоде добавлены в базу "weather.db"')


if __name__ == '__main__':
    menu = Menu()
    while True:
        menu.get_info()
        menu.get_info_answer()


