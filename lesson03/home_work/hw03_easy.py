__author__ = 'Кусый Андрей Геннадьевич'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    
    x =  number * 10 ** (ndigits + 1) % 10 // 1
    rez = number * 10 ** ndigits // 1
    
    if x >= 5:
        return (rez + 1) / 10 ** ndigits
    else:
        return rez / 10 ** ndigits


print(my_round(2.12345673, 4))
print(my_round(2.19999673, 5))
print(my_round(2.99999673, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    
    left_part = ticket_number // 100000 % 10 + ticket_number // 10000 % 10 + ticket_number // 1000 % 10
    right_part = ticket_number // 100 % 10 + ticket_number // 10 % 10 + ticket_number % 10
    
    return left_part == right_part
    
    #if left_part == right_part:
    #    return 'Счастливый'
    #else:
    #    return 'Несчастливый'

print(lucky_ticket(123006))
print(lucky_ticket(123214))
print(lucky_ticket(436751))
