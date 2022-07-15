import random
from classes import Player


def print_card(cards, name_player):
    """
    Печатаем карточки
    :param name_player:
    :param cards: Словарь с картами
    :return:
    """
    for key, val in cards.items():
        print(name_player, key)
        print('- ' * 13)
        num = list(val.numbers)
        for x in num:
            for i, y in enumerate(x):
                print((' ' if i == 0 else '  ') if y == '_' else y, end=' ')
            print()
        print('- ' * 13)


def add_player(player, amount, player_type=False):
    name_play = f'Игрок {player} Человек' \
        if player_type else f'Игрок {player} Компьютер'
    comp = Player()
    comp.app_card(amount=amount)
    computer_cards = comp.cards
    return computer_cards, name_play


def check_cards(cards, number, del_number=False):
    result = []
    for key in cards.keys():
        if number in cards[key].linked_lists:
            if del_number:
                cards[key].del_number(number)
            result.append(True)
        else:
            result.append(False)
    return True if True in result else False


def step_player(player_cards, move, answer=''):
    if answer == 'y':
        if check_cards(player_cards, move):
            check_cards(player_cards, next_move, del_number=True)
            return True
        else:
            return False
    elif answer == 'n':
        return False if check_cards(player_cards, move) else True


def game_over(cards):
    result = []
    for key in cards.keys():
        result.append(True) if cards[key].game_check() else result.append(False)
    return True if True in result else False


if __name__ == '__main__':
    game = False
    moves = [i for i in range(1, 91)]
    random.shuffle(moves)
    game_moves = (i for i in moves)
    print('== Игра Лото ==')
    print('1 - Выбрать игроков;\n'
          '2 - Начать игру;\n'
          '0 - Выйти из игры.')

    menu, player_menu, cards_menu = 99, 99, 99
    one_player_cards, two_player_cards = [], []
    one_player_name, two_player_name = [], []

    while menu:
        try:
            menu = int(input('Выберите пункт меню: '))
            if menu == 2 and not one_player_cards:
                print('Для начала, выберите игроков')
                menu = 99
        except ValueError:
            print('Это не является числом!')
            menu = 99

        if menu == 1:
            under_menu_1 = True
            while under_menu_1:
                print('Выберите следующие варианты игры:\n'
                      '1 - Компьютер - Человек\n'
                      '2 - Компьютер - Компьютер\n'
                      '3 - Человек - Человек\n')
                try:
                    player_menu = int(input('Какой пункт выбираете? '))
                except ValueError:
                    print('Это не является числом! Повторим.')

                if 1 <= player_menu <= 4:
                    under_menu_1 = False
                else:
                    print('Нет такого пункта')

            under_menu_2 = True
            while under_menu_2:
                try:
                    cards_menu = int(input('По сколько карточек желаете? '))
                except ValueError:
                    print('Это не является числом! Повторим.')

                if cards_menu >= 1:
                    under_menu_2 = False
                else:
                    print('Слишком мало для игры')

            if player_menu == 1 or player_menu == 2:
                one_player_cards, one_player_name = add_player(1, cards_menu)
                print_card(one_player_cards, one_player_name)
            elif player_menu == 3:
                one_player_cards, one_player_name = add_player(1, cards_menu,
                                                               player_type=True)
                print_card(one_player_cards, one_player_name)

            if player_menu == 1 or player_menu == 3:
                two_player_cards, two_player_name = add_player(2, cards_menu,
                                                               player_type=True)
                print_card(two_player_cards, two_player_name)
            elif player_menu == 2:
                two_player_cards, two_player_name = add_player(2, cards_menu)
                print_card(two_player_cards, two_player_name)

        elif menu == 2:
            game = True
            break

    while game:
        print_card(one_player_cards, one_player_name)
        print('# ' * 15)
        print_card(two_player_cards, two_player_name)
        try:
            next_move = next(game_moves)
        except StopIteration:
            break

        print(f'Выпал боченок № {next_move}')

        if player_menu == 1:
            if check_cards(one_player_cards, next_move):
                check_cards(one_player_cards, next_move, del_number=True)
            in_del = ''
            while in_del != 'y' and in_del != 'n':
                in_del = input(f'Ход {two_player_name}.'
                               f' Зачеркнуть цифру? (y/n) ')

            if not step_player(two_player_cards, next_move, in_del):
                print(f'{two_player_name}, Вы проиграли')
                break
        elif player_menu == 2:
            if check_cards(one_player_cards, next_move):
                check_cards(one_player_cards, next_move, del_number=True)
            if check_cards(two_player_cards, next_move):
                check_cards(two_player_cards, next_move, del_number=True)
        elif player_menu == 3:
            in_del = input(f'Ход {one_player_name}. Зачеркнуть цифру? (y/n) ')
            if not step_player(one_player_cards, next_move, in_del):
                print(f'Игрок {one_player_name}, Вы проиграли')
                break
            in_del = input(f'Ход {two_player_name}. Зачеркнуть цифру? (y/n) ')
            if not step_player(two_player_cards, next_move, in_del):
                print(f'Игрок {two_player_name}, Вы проиграли')
                break

        if game_over(one_player_cards) and game_over(two_player_cards):
            print_card(one_player_cards, one_player_name)
            print('# ' * 15)
            print_card(two_player_cards, two_player_name)
            print(f'Это ничья!')
            break
        elif game_over(one_player_cards):
            print_card(one_player_cards, one_player_name)
            print('# ' * 15)
            print_card(two_player_cards, two_player_name)
            print(f'Выиграл {one_player_name}')
            break
        elif game_over(two_player_cards):
            print_card(one_player_cards, one_player_name)
            print('# ' * 15)
            print_card(two_player_cards, two_player_name)
            print(f'Выиграл {two_player_name}')
            break

    print('Конец игры')
