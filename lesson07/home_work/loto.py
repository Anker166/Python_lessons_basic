#!/usr/bin/python3

"""
== Лото ==
Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random

numbers = [i for i in range(1, 91)]


class Ticket:

    def __init__(self):
        self.ticket = [['' for _ in range(9)] for _ in range(3)]
        self.ticket_numbers = random.sample(numbers[:], 15)
        __index = [_ for _ in range(9)]
        __position_index = []
        __position_number = []

        for i in range(0, 11, 5):
            __position_number.extend([sorted(self.ticket_numbers[i:i + 5])])
        for i in range(3):
            __position_index.extend([sorted(random.sample(__index[:], 5))])

        for i in range(3):
            for j in range(5):
                self.ticket[i][__position_index[i][j]] = __position_number[i][j]

    def get_ticket_nums(self):
        return self.ticket_numbers

    def print_ticket(self, n='Player'):
        if n == 'Computer':
            print(f' Карточка компьютера '.center(26, '-'))
        else:
            print(f' Ваша карточка '.center(26, '-'))
        for row in self.ticket:
            for el in row:
                print(f'{el}'.rjust(2), end=' ')
            print()
        print('-' * 26)

    def check_number(self, num, ans):
        if ans == 'y':
            if num in self.ticket[0] or num in self.ticket[1] or num in self.ticket[2]:
                for i in range(3):
                    if num in self.ticket[i]:
                        self.ticket[i][self.ticket[i].index(num)] = '-'
                        self.ticket_numbers.remove(num)
                return True
            else:
                print('Вы проиграли')
                return False
        elif ans == 'n':
            if num in self.ticket[0] or num in self.ticket[1] or num in self.ticket[2]:
                print('Вы проиграли')
                return False
            else:
                return True

    def check_number_comp(self, num):
        for i in range(3):
            if num in self.ticket[i]:
                self.ticket[i][self.ticket[i].index(num)] = '-'
                self.ticket_numbers.remove(num)


def new_num():
    kegs = numbers[:]
    random.shuffle(kegs)
    for num in kegs:
        yield num, len(kegs) - (kegs.index(num) + 1)


def check_answer():
    while True:
        answer = input('Зачеркнуть цифру? (y/n)\n').lower()
        if answer == 'y' or answer == 'n':
            break
        else:
            print('Вы ввели неправильную команду, попробуйте снова!')
    return answer


def info(x):
    text_info = ['Старт игры', 'Новый раунд',
                 'Победили оба игрока', 'Победил игрок',
                 'Победил компьютер',
                 ]
    print('♦' * 26)
    print(f'{text_info[x]}'.center(26, '-'))
    print('♦' * 26)


player_ticket = Ticket()
computer_ticket = Ticket()


info(0)

for number, residue in new_num():
    print(f'Новый бочонок: {number} (Осталось: {residue})')
    player_ticket.print_ticket()
    computer_ticket.print_ticket('Computer')
    player_answer = check_answer()
    if not player_ticket.check_number(number, player_answer):
        break
    # player_ticket.check_number_comp(number)
    computer_ticket.check_number_comp(number)
    if len(player_ticket.get_ticket_nums()) == 0 and len(computer_ticket.get_ticket_nums()) == 0:
        info(2)
        player_ticket.print_ticket()
        computer_ticket.print_ticket('Computer')
        break
    elif len(player_ticket.get_ticket_nums()) == 0:
        info(3)
        player_ticket.print_ticket()
        computer_ticket.print_ticket('Computer')
        break
    elif len(computer_ticket.get_ticket_nums()) == 0:
        info(4)
        player_ticket.print_ticket()
        computer_ticket.print_ticket('Computer')
        break
    info(1)