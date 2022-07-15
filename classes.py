"""
Класс создания случайной карточки.
Класс создания игрока и что он может (класс человек и класс компьютер).
"""
import random


class PlayingCard:
    def __init__(self):
        self.numbers = []
        self.linked_lists = []

    def filling(self):
        """
        Добавляет значения в карточку.
        :return: Возвращает список из 15 значений.
        """
        self.numbers = [['_' for _ in range(9)] for _ in range(3)]
        for i in range(3):
            line_of_digits = []
            while len(line_of_digits) != 5:
                num = random.randint(0, 8)
                if num not in line_of_digits:
                    line_of_digits.append(num)
            line_of_digits.sort()
            for j in line_of_digits:
                while True:
                    number = random.randint(j * 10 + 1, j * 10 + 9)
                    if number not in self.linked_lists:
                        self.linked_lists.append(number)
                        self.numbers[i][j] = number
                        break

    def number_check(self, number):
        """
        Проверяет, есть ли такая цифра.
        :param number: Цифра, которую нужно проверить.
        :return: Возвращает True если цифра есть в карточке,
        False - если цифры в карточке нет.
        """
        return True if number in self.linked_lists else False

    def game_check(self):
        """
        Проверяет есть ли еще не закрытые цифры.
        :return: True - все закрыты.
        """
        dash = 0
        for numbers in self.numbers:
            dash += numbers.count('-')
            dash += numbers.count('- ')
        return True if len(self.linked_lists) == dash else False

    def del_number(self, number):
        for lists in self.numbers:
            if number in lists:
                address = lists.index(number)
                lists[address] = '-' if address == 0 else '- '


class Player:
    def __init__(self):
        self.num_card = 1
        self.cards = {}

    def app_card(self, amount=1):
        """
        Добавляет карту для игры.
        :return: Массив 3 на 9 с цифрами и '-', где цифры нет.
        """
        for i in range(amount):
            card = PlayingCard()
            card.filling()
            self.cards[f'Карточка {i+1}'] = card


if __name__ == '__main__':
    pass
