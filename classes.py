"""
Класс создания случайной карточки.
Класс создания игрока и что он может (класс человек и класс компьютер).
"""
import random


class PlayingCard:
    """
    Класс Карта
    """
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


class Player:
    """
    Класс Игрок
    """
    def __init__(self):
        self.num_card = 1
        self.cards = {}
        self.name = ''

    def app_cards(self, amount=1):
        """
        Добавляет карту или карты для игры.
        :param amount: Сколько карт нужно добавить.
        :return: Массив 3 на 9 с цифрами и '-', где цифры нет.
        """
        for i in range(amount):
            card = PlayingCard()
            card.filling()
            self.cards[f'Карточка {i+1}'] = card

    def barrel_check(self, barrel_number, del_number=False):
        """
        Проверяет, есть ли такая цифра.
        :param del_number: Нужно ли удалять цифру при проверке, True - нужно.
        :param barrel_number: Цифра, которую нужно проверить.
        :return: Возвращает True если цифра есть в карточке,
        False - если цифра в карточке/карточках нет.
        """
        result = []
        for val in self.cards.values():
            for value in val.numbers:
                result.append(True if barrel_number in value else False)
                if barrel_number in value and del_number:
                    address = value.index(barrel_number)
                    value[address] = '-' if address == 0 else '- '
        return True if True in result else False

    def game_check(self):
        """
        Проверяет есть ли еще не закрытые цифры.
        :return: True - все закрыты, конец игре
        """
        result = []
        for key, val in self.cards.items():
            dash = 0
            for value in val.numbers:
                dash += value.count('-')
                dash += value.count('- ')
            result.append(True if dash == 15 else False)
        return True if True in result else False


if __name__ == '__main__':
    print('Классы для игры Лото')
