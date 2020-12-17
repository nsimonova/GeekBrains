# == Лото ==
#
# Правила игры в лото.
#
# Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
#
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
#
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
#
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
#
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
#
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
#
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
#     Если цифра есть на карточке - она зачеркивается и игра продолжается.
#     Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
#     Если цифра есть на карточке - игрок проигрывает и игра завершается.
#     Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
#
# Пример одного хода:
#
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 87     - 14    11
#       16 49    55 88    77
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
#
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать
# с помощью функции-генератора.
#
# Подсказка: для работы с псевдослучайными числами удобно использовать
# модуль random: http://docs.python.org/3/library/random.html
from random import Random


class LottoCard:
    def __init__(self, autoplay, player_name):
        self.autoplay = autoplay
        self.player_name = player_name
        self.card = self._generate_card()
        self.not_striked_out_count = 15

    def _generate_numbers(self, count, min, max):
        numbers = []
        r = Random()
        while len(numbers) < count:
            number = r.randint(min, max)
            if numbers.count(number) == 0:
                numbers.append(number)
        return numbers

    def _generate_card(self):
        card = []
        numbers = self._generate_numbers(15, 1, 90)
        for row_num in range(0, 3):
            row = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
            row_digits = numbers[5*row_num:5*row_num+5]
            row_digits.sort()
            places = self._generate_numbers(5, 0, 8)
            places.sort()
            for index, number in enumerate(row_digits):
                row[places[index]] = number
            card.append(row)
        return card

    def __str__(self):
        title_start = (46 - len(self.player_name)) // 2
        title = ('-' * title_start) + self.player_name + ('-' * (46 - title_start - len(self.player_name)))
        footer = '-' * 46
        result = title + '\n'
        for row in self.card:
            row_str = '| '
            for digit in row:
                if type(digit) == int:
                    if digit < 10:
                        row_str += " "
                    row_str += str(digit)
                else:
                    row_str += digit
                row_str += ' | '
            result += row_str + '\n'
        result += footer + '\n'
        return result

    def strike_out_if_exists(self, number):
        row_num = -1
        num_in_row = -1
        exists = False
        for i, row in enumerate(self.card):
            if row.count(number) > 0:
                exists = True
                row_num = i
                num_in_row = row.index(number)
        decision = ''
        if not self.autoplay:
            decision = input('Зачеркнуть цифру? (y/n) ').lower()
            if decision != 'y' and decision != 'n':
                print("Разрешено вводить только y/n")
                return False
        if exists and (decision == 'y' or self.autoplay):
            self.card[row_num][num_in_row] = '--'
            self.not_striked_out_count += -1
        elif (exists and decision == 'n') or (not exists and decision == 'y'):
            return False
        return True

    def is_all_striked_out(self):
        return self.not_striked_out_count == 0


class Lotto:
    def __init__(self, player_name):
        self.player_card = LottoCard(False, player_name)
        self.computer_card = LottoCard(True, 'Computer')

    def play(self):
        print('Начало игры! Сыграем в лото! \n')
        barrels = list(range(1, 91))
        r = Random()
        while len(barrels) > 0:
            index = r.randint(0, len(barrels) - 1)
            current_barrel = barrels[index]
            print('Новый бочонок: ' + str(current_barrel) + ' (осталось ' + str(len(barrels) - 1) + ')')
            print(self.player_card)
            print(self.computer_card)
            if not self.player_card.strike_out_if_exists(current_barrel):
                print('Вы проиграли!')
                break
            self.computer_card.strike_out_if_exists(current_barrel)
            if self.player_card.is_all_striked_out():
                print('Вы победили!')
                break
            if self.computer_card.is_all_striked_out():
                print('Компьютер победил!')
                break
            barrels.pop(index)


game = Lotto(input('Введите ваше имя '))
game.play()
