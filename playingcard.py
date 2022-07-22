"""
Класс создания случайной карточки.
"""
import random


class PlayingCard:
    """
    Класс Карта
    """

    def __init__(self):
        self._numbers = []
        self._linked_lists = []

    def format_card(self):
        """
        Меняет формат карты, объединяя строки и удаляя места где
        не стояли цифры.
        :return: Список из 15 значений.
        """
        result = []
        for numbers in self.card:
            result += [i for i in numbers if isinstance(i, int)]
        return result

    @property
    def card(self):
        """
        Дает доступ к карте, без скобок в конце.
        :return: Список 3 на 9
        """
        return self._numbers

    def filling(self):
        """
        Добавляет значения в карточку.
        :return: Возвращает список из 27 значений - 3 строки по 9 значений.
        """
        self._numbers = [['_' for _ in range(9)] for _ in range(3)]
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
                    if number not in self._linked_lists:
                        self._linked_lists.append(number)
                        self._numbers[i][j] = number
                        break

    def __str__(self):
        """
        Возвращает в одной строке список цифр и полный вид карты.
        :return: Строка
        """
        return f'{self._linked_lists} - {self._numbers}'

    def __eq__(self, other):
        """
        Сравнивает 2 карты на количество не закрытых цифр.
        :param other: Вторая карта.
        :return: True - равны, False - карты не равны.
        """
        return len([i for i in self.format_card() if isinstance(i, int)]) ==\
               len([i for i in other.format_card() if isinstance(i, int)])


if __name__ == '__main__':
    print('Классы для игры Лото, PlayingCard')
