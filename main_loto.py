import random
from player import Player


def print_card(cards, name_player):
    """
    Выводит карточки.
    :param name_player: Имя игрока.
    :param cards: Словарь с картами.
    :return:
    """
    for key, val in cards.items():
        print(name_player, key)
        print('- ' * 13)
        for x in val:
            for i, y in enumerate(x):
                print((' ' if i == 0 else '  ') if y == '_' else y, end=' ')
            print()
        print('- ' * 13)


def add_player(player_number, amount, player_type=False):
    """
    Инициализацию игрока и добавление карточек к нему.
    :param player_number: Номер.
    :param amount: Количество карточек.
    :param player_type: Тип игрока, Человек или Компьютер.
    :return: Словарь карт и имя игрока.
    """
    player = Player()
    player.name = f'Игрок {player_number} Человек' \
        if player_type else f'Игрок {player_number} Компьютер'
    player.app_cards(amount=amount)
    return player


def step_player(player, move, answer=''):
    """
    Проверка игрока на каждом шаге.
    :param player: Игрок.
    :param move: Цифра на боченке.
    :param answer: Ответ игрока об удалении цифры.
    :return: True False.
    """
    if answer == 'y':
        if player.barrel_check(move):
            player.barrel_check(move, del_number=True)
            return True
        else:
            return False
    elif answer == 'n':
        return False if player.barrel_check(move) else True


def auto_check(player, move):
    """
    Проверяет и удаляет цифру
    :param player: Игрок
    :param move: Цифра
    :return: None
    """
    # TODO
    if move in player:
        player.barrel_check(move, del_number=True)
    # if player.barrel_check(move):
    #     player.barrel_check(move, del_number=True)


if __name__ == '__main__':

    print('== Игра Лото ==')
    print('1 - Выбрать игроков;\n'
          '2 - Начать игру;\n'
          '0 - Выйти из игры.')

    menu, player_menu, cards_menu = 99, 99, 99
    one_player, two_player = '', ''

    while menu:
        try:
            menu = int(input('Выберите пункт меню: '))
            if menu == 2 and not one_player:
                print('Для начала, выберите игроков')
                menu = 99
        except ValueError:
            print('Это не является числом!')
            menu = 99

        if menu == 1:
            while True:
                print('Выберите следующие варианты игры:\n'
                      '1 - Компьютер - Человек\n'
                      '2 - Компьютер - Компьютер\n'
                      '3 - Человек - Человек\n')
                try:
                    player_menu = int(input('Какой пункт выбираете? '))
                except ValueError:
                    print('Это не является числом! Повторим.')
                if 1 <= player_menu <= 3:
                    break
                else:
                    print('Нет такого пункта')

            while True:
                try:
                    cards_menu = int(input('По сколько карточек желаете? '))
                except ValueError:
                    print('Это не является числом! Повторим.')
                if cards_menu >= 1:
                    break
                else:
                    print('Слишком мало для игры')

            if player_menu == 1 or player_menu == 2:
                one_player = add_player(1, cards_menu)
                print_card(one_player.cards, one_player.name)
            elif player_menu == 3:
                one_player = add_player(1, cards_menu, player_type=True)
                print_card(one_player.cards, one_player.name)

            if player_menu == 1 or player_menu == 3:
                two_player = add_player(2, cards_menu, player_type=True)
                print_card(two_player.cards, two_player.name)
            elif player_menu == 2:
                two_player = add_player(2, cards_menu)
                print_card(two_player.cards, two_player.name)

        elif menu == 2:
            game = False
            moves = [i for i in range(1, 91)]
            random.shuffle(moves)
            game_moves = (i for i in moves)
            steps = 0
            while True:
                print_card(one_player.cards, one_player.name)
                print('# ' * 15)
                print_card(two_player.cards, two_player.name)
                try:
                    next_move = next(game_moves)
                except StopIteration:
                    break
                steps += 1
                print(f'Ход № {steps}, Выпал боченок № {next_move}')
                if player_menu == 1:
                    auto_check(one_player, next_move)
                    in_del = ''
                    while in_del != 'y' and in_del != 'n':
                        in_del = input(f'Ход {two_player.name}.'
                                       f' Зачеркнуть цифру? (y/n) ')
                    if not step_player(two_player, next_move, answer=in_del):
                        print(f'{two_player.name}, Вы проиграли')
                        break
                elif player_menu == 2:
                    auto_check(one_player, next_move)
                    auto_check(two_player, next_move)
                elif player_menu == 3:
                    in_del = ''
                    while in_del != 'y' and in_del != 'n':
                        in_del = input(f'Ход {one_player.name}.'
                                       f' Зачеркнуть цифру? (y/n) ')
                    if not step_player(one_player, next_move, answer=in_del):
                        print(f'Игрок {one_player.name}, Вы проиграли')
                        break
                    in_del = ''
                    while in_del != 'y' and in_del != 'n':
                        in_del = input(f'Ход {two_player.name}.'
                                       f' Зачеркнуть цифру? (y/n) ')
                    if not step_player(two_player, next_move, answer=in_del):
                        print(f'Игрок {two_player.name}, Вы проиграли')
                        break

                if one_player.game_check() and two_player.game_check():
                    print_card(one_player.cards, one_player.name)
                    print('# ' * 15)
                    print_card(two_player.cards, two_player.name)
                    print(f'Это ничья!')
                    break
                elif one_player.game_check():
                    print_card(one_player.cards, one_player.name)
                    print('# ' * 15)
                    print_card(two_player.cards, two_player.name)
                    print(f'Выиграл {one_player.name}')
                    break
                elif two_player.game_check():
                    print_card(one_player.cards, one_player.name)
                    print('# ' * 15)
                    print_card(two_player.cards, two_player.name)
                    print(f'Выиграл {two_player.name}')
                    break

    print('Конец игры')
