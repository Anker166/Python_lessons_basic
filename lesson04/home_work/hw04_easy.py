# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

origin_lst = [1, 2, 4, 0, 9, 7, 5, 3, 6]
modified_lst = [i ** 2 for i in origin_lst]
print(modified_lst)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits1 = ['банан', 'апельсин', 'ананас', 'киви', 'яблоко']
fruits2 = ['апельсин', 'киви', 'маракуйя', 'арбуз']
fruits3 = [i for i in fruits1 if i in fruits2]
print(fruits3)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random

first_lst = [random.randint(-100, 100) for i in range(15)]
print(first_lst)
second_lst = [i for i in first_lst if not i % 3 and i > 0 and i % 4]
print(second_lst)