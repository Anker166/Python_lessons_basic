__author__ = 'Кусый Андрей Геннадьевич'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m): # предположил, что элементы будут запрашиваться с 1, а не с 0
    fib = [1, 1]
    for i in range(2, m):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n - 1:m]

print(fibonacci(5, 10))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    i = 0
    step = 0
    while i < len(origin_list):
        if i + 1 != len(origin_list) and origin_list[i] > origin_list[i + 1]:
            origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
            step = 1
        i += 1
        if i == len(origin_list) and step == 1:
            step = 0
            i = 0
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(my_func, my_list):
    rez = []
    if my_func == None:
        for elem in my_list:
            if elem:
                rez.append(elem) 
    else:
        for elem in my_list:
            if my_func(elem):
                rez.append(elem)      
    return rez

print (my_filter(lambda x : x > 5, [2, 10, -10, 8, 2, 0, 14]))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

import math

def length_AB(A, B):
    return math.sqrt((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2)

A1 = [1, 1]
A2 = [6, 1]
A3 = [4, 3]
A4 = [3, 3]
step = 0

while True:
    if length_AB(A1, A2) == length_AB(A3, A4) and length_AB(A2, A3) == length_AB(A4, A1):
        print('Эти точки будут вершинами параллелограмма')
        break
    step += 1
    if step == 1:
        A2, A3 = A3, A2
    elif step == 2:
        A2, A3, A4 = A3, A4, A2
    else:
        print('Эти точки не будут вершинами параллелограмма')
        break

