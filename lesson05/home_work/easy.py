import os


def change_dir(name):
    path_old = os.getcwd()
    path_now = os.path.join(path_old, name)
    try:
        os.chdir(path_now)
    except OSError as e:
        print(f'Невозможно перейти в папку {name}!\nОшибка: {e}')
    else:
        print(f'Вы успешно перешли в папку {name}!')


def all_elements():
    path_old = os.getcwd()
    elements = os.listdir(path_old)
    print(f'Содержимое текущей папки {path_old}:')
    for elem in elements:
        print(elem)


def remove_dirs(name):
    path_old = os.getcwd()
    path_now = os.path.join(path_old, name)
    try:
        os.rmdir(path_now)
    except OSError as e:
        print(f'Невозможно удалить папку {name}!\nОшибка: {e}')
    else:
        print(f'Папка {name} успешно удалена!')


def make_dirs(name):
    path_old = os.getcwd()
    path_now = os.path.join(path_old, name)
    try:
        os.mkdir(path_now)
    except OSError as e:
        print(f'Невозможно создать папку {name}!\nОшибка: {e}')
    else:
        print(f'Папка {name} успешно создана!')
