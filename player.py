"""
Класс создания игрока и что он может (класс человек и класс компьютер).
"""
from playingcard import PlayingCard


class Player:
    """
    Класс Игрок
    """

    def __init__(self):
        self._cards = {}
        self._only_numbers = []
        self._name = ''

    @property
    def name(self):
        """
        Возвращает имя игрока.
        :return: Имя игрока.
        """
        return self._name

    @name.setter
    def name(self, new_name):
        """
        Изменяет имя игрока.
        :param new_name: Новое имя.
        :return: None
        """
        self._name = new_name

    @property
    def cards(self):
        """
        Возвращает словарь карт.
        :return: Словарь карт.
        """
        return self._cards

    @property
    def only_numbers(self):
        """
        Возвращает только цифры от крт.
        :return: Список списков карт.
        """
        return self._only_numbers

    def data_cards(self):
        """
        Возвращает один список на 1 карту, только цифры.
        :return: Список цифр каждой карты
        """
        result = []
        for value_card in self._cards.values():
            temp_list = []
            for value_line in value_card:
                for number in value_line:
                    if isinstance(number, int):
                        temp_list.append(number)
            result.append(temp_list)
        return result

    def app_cards(self, amount=1):
        """
        Добавляет карту или карты для игры.
        :param amount: Сколько карт нужно добавить.
        :return: Массив 3 на 9 с цифрами и '-', где цифры нет.
        """
        for i in range(amount):
            card = PlayingCard()
            card.filling()
            self.cards[f'Карточка {i + 1}'] = card.card
        self._only_numbers = self.data_cards()

    def barrel_check(self, barrel_number, del_number=False):
        """
        Проверяет, есть ли такая цифра.
        :param del_number: Нужно ли удалять цифру при проверке, True - нужно.
        :param barrel_number: Цифра, которую нужно проверить.
        :return: Возвращает True если цифра есть в карточке,
        False - если цифра в карточке/карточках нет.
        """
        result = []
        for card in self._cards.values():
            for line_card in card:
                result.append(True if barrel_number in line_card else False)
                if barrel_number in line_card and del_number:
                    address = line_card.index(barrel_number)
                    line_card[address] = '-' if address == 0 else '- '
        return True if True in result else False

    def game_check(self):
        """
        Проверяет есть ли еще не закрытые цифры.
        :return: True - все закрыты, конец игре
        """
        result = []
        for val in self.cards.values():
            dash = 0
            for value in val:
                dash += value.count('-')
                dash += value.count('- ')
            result.append(True if dash == 15 else False)
        return True if True in result else False

    def __str__(self):
        """
        Возвращает строку с Именем игрока и всеми его картами.
        :return: Строка
        """
        return f'Name - {self._name} - {self._cards}'

    def __contains__(self, item):
        one_list = []
        for card in self.only_numbers:
            for num in card:
                if isinstance(num, int):
                    one_list.append(num)
        return True if item in one_list else False

    def __ge__(self, other):
        """
        Сравнивает количество не закрытых цифр на картах игроков.
        self a >= other
        :param other: Другой игрок
        :return: True - верно, False - нет
        """
        def app_number(card):
            numbers = []
            for one_card in card.values():
                for line_card in one_card:
                    for element in line_card:
                        if isinstance(element, int):
                            numbers.append(element)
            return numbers
        return len(app_number(self._cards)) >= len(app_number(other._cards))

    def __eq__(self, other):
        """
        Сравнивает 2 игроков по количеству не закрытых цифр на картах.
        :param other: Другой игрок.
        :return: True - одинаковое количество не закрытых цифр, False - разное.
        """
        def app_number(card):
            numbers = []
            for one_card in card.values():
                for line_card in one_card:
                    for element in line_card:
                        if isinstance(element, int):
                            numbers.append(element)
            return numbers
        return len(app_number(self._cards)) == len(app_number(other._cards))

    def __len__(self):
        result = []
        for card in self.cards.values():
            for line_card in card:
                for number in line_card:
                    if isinstance(number, int):
                        result.append(number)
        return len(result)


if __name__ == '__main__':
    print('Классы для игры Лото, Player')
