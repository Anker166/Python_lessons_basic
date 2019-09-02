# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Human:
    def __init__(self, name, surname, patronymic):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    def get_full_name(self):
        return self.surname + ' ' + self.name + ' ' + self.patronymic


class Pupil(Human):
    def __init__(self, name, surname, patronymic, father, mother, school_classes):
        Human.__init__(self, name, surname, patronymic)
        self.father = father
        self.mother = mother
        self.school_classes = school_classes

    def get_full_name(self):
        return self.surname + ' ' + self.name[0] + '.' + self.patronymic[0] + '.'


class Parent(Human):
    def __init__(self, name, surname, patronymic, par_type):
        Human.__init__(self, name, surname, patronymic)
        self.par_type = par_type


class Teacher(Human):
    def __init__(self, name, surname, patronymic, subject, school_classes):
        Human.__init__(self, name, surname, patronymic)
        self.subject = subject
        self.school_classes = school_classes


class_rooms = ['10 А', '10 Б', '10 В']

parents = [Parent('Максим', 'Иванов', 'Иванович', 'Отец'),
           Parent('Елена', 'Иванова', 'Ивановна', 'Мать'),
           Parent('Евгений', 'Петров', 'Петрович', 'Отец'),
           Parent('Евгения', 'Петрова', 'Петровна', 'Мать'),
           Parent('Владимир', 'Сидоров', 'Михайлович', 'Отец'),
           Parent('Людмила', 'Сидорова', 'Михайловна', 'Мать'),
           Parent('Дмитрий', 'Козлов', 'Дмитриевич', 'Отец'),
           Parent('Оксана', 'Козлова', 'Дмитриевна', 'Мать'),
           Parent('Василий', 'Бобров', 'Васильевич', 'Отец'),
           Parent('Василиса', 'Боброва', 'Васильевна', 'Мать'),
           Parent('Александр', 'Снегирев', 'Александрович', 'Отец'),
           Parent('Александра', 'Снегирева', 'Александровна', 'Мать'),
           ]

students = [Pupil('Леонид', 'Иванов', 'Максимович', parents[0], parents[1], class_rooms[0]),
            Pupil('Геркулес', 'Петров', 'Евгеньевич', parents[2], parents[3], class_rooms[0]),
            Pupil('Партокл', 'Сидоров', 'Владимирович', parents[4], parents[5], class_rooms[1]),
            Pupil('Платон', 'Козлов', 'Дмитриевич', parents[6], parents[7], class_rooms[1]),
            Pupil('Герон', 'Бобров', 'Васильевич', parents[8], parents[9], class_rooms[2]),
            Pupil('Аид', 'Снегирев', 'Александрович', parents[10], parents[11], class_rooms[2]),
            ]

teachers = [Teacher('Апогей', 'Карасев', 'Ненастьевич', 'Математика', class_rooms),
            Teacher('Людовиг', 'Австрийский', 'Демиургович', 'История', [class_rooms[0], class_rooms[2]]),
            Teacher('Мерлин', 'Звездочетов', 'Игоревич', 'Алхимия', [class_rooms[1], class_rooms[2]]),
            ]


print('Список всех классов школы:')
for elem in class_rooms:
    print(elem)

print('Список всех учеников в классе')
answer_class = input('Введите номер класса из списка всех классов школы:\n').upper()
if answer_class in class_rooms:
    for elem in students:
        if elem.school_classes == answer_class:
            print(elem.get_full_name())
else:
    print('Вы ввели неправильный номер класса')

print('Список всех предметов указанного ученика')
answer_pup = input('Введите фамилию и иницалы ученика:\n').title()
for pup in students:
    if answer_pup == pup.get_full_name():
        for teach in teachers:
            if pup.school_classes in teach.school_classes:
                print(teach.subject)

print('ФИО родителей указанного ученика')
answer_pup = input('Введите фамилию и иницалы ученика:\n').title()
for pup in students:
    if answer_pup == pup.get_full_name():
        print(f'{pup.father.par_type}: {pup.father.get_full_name()}')
        print(f'{pup.mother.par_type}: {pup.mother.get_full_name()}')

print('Список всех учителей класса')
answer_class = input('Введите номер класса из списка всех классов школы:\n').upper()
for teach in teachers:
    if answer_class in teach.school_classes:
            print(teach.get_full_name())