# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import sys
import os
import shutil




def make_dirs(names):
    path_old = os.getcwd()
    for elem in x:
        path_now = os.path.join(path_old, elem)
        os.mkdir(path_now)


def remove_dirs(names):
    path_old = os.getcwd()
    dirs = os.listdir(path_old)
    for elem in dirs:
        if elem in x:
            path_now = os.path.join(path_old, elem)
            os.rmdir(path_now)


x = [f'dir_{i}' for i in range(1, 10)]
make_dirs(x)
remove_dirs(x)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def all_dirs():
    path_old = os.getcwd()
    elements = os.listdir(path_old)
    print(f'Список папок в директории {path_old}:')
    for i in elements:
        path_now = os.path.join(path_old, i)
        if os.path.isdir(path_now):
            print(i)


all_dirs()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def file_copy():
    file_name = sys.argv[0]
    file_name_new = file_name[:file_name.rfind('.')] + '(copy)' + file_name[file_name.rfind('.'):]
    shutil.copy(file_name, file_name_new)


file_copy()
