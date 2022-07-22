from playingcard import PlayingCard
from player import Player
from main_loto import add_player, step_player, auto_check


class TestPlayingCard:

    def setup(self):
        self.first_card = PlayingCard()
        self.second_card = PlayingCard()

    def test_init(self):
        assert self.first_card.card == []

    def test_str(self):
        self.first_card.filling()
        assert isinstance(str(self.first_card), str)

    def test_format_card(self):
        self.first_card.filling()
        assert len(self.first_card.format_card()) == 15

    def test_eg(self):
        self.first_card.filling()
        self.second_card.filling()
        assert self.first_card == self.second_card

    def test_card(self):
        self.first_card.filling()
        self.second_card.filling()
        assert len(self.first_card.card) == len(self.second_card.card)

    def test_filling(self):
        self.first_card.filling()
        assert len(self.first_card.card) == 3
        assert len(self.first_card.card[0]) == 9
        assert len(self.first_card.card[1]) == 9
        assert len(self.first_card.card[2]) == 9
        assert self.first_card.card[0].count('_') == 4
        assert self.first_card.card[1].count('_') == 4
        assert self.first_card.card[2].count('_') == 4
        # Тест.
        for numbers in self.first_card.card:
            variable = numbers
            for _ in range(4):
                variable.remove('_')
            for num in variable:
                assert 90 >= num > 0


class TestPlayer:

    def setup(self):
        self.player = Player()

    def teardown(self):
        del self.player

    def test_init(self):
        assert isinstance(self.player.cards, dict)
        assert self.player.name == ''
        assert self.player.only_numbers == []

    def test_name(self):
        self.player.name = 'Player_first'
        assert self.player.name == 'Player_first'

    def test_new_name(self):
        self.player.name = 'Player_second'
        assert self.player.name == 'Player_second'

    def test_cards(self):
        amount = 2
        self.player.app_cards(amount=amount)
        for i, data in enumerate(self.player.cards.items()):
            assert data[0] == f'Карточка {i + 1}'
            assert len(data[1]) == 3

    def test_data_cards(self):
        self.player.app_cards()
        assert len(self.player.data_cards()) == 1
        assert len(self.player.data_cards()[0]) == 15
        self.player.barrel_check(self.player.only_numbers[0][0],
                                 del_number=True)
        assert len(self.player.data_cards()[0]) == 14

    def test_only_numbers(self):
        self.player.app_cards()
        assert len(self.player.only_numbers) == 1
        assert len(self.player.only_numbers[0]) == 15

    def test_str(self):
        assert isinstance(str(self.player), str)

    def test_app_cards(self):
        amount = 1
        self.player.app_cards(amount=amount)
        # Тест.
        barrel = [i for i in range(1, 91)]
        result = []
        for card_numbers in self.player.only_numbers:
            for num in card_numbers:
                result.append(True if num in barrel else False)
        assert result.count(True) == 15
        # Тест.
        amount = 5
        self.player.app_cards(amount=amount)
        assert len(self.player.cards) == amount
        for i, key in enumerate(self.player.cards.keys()):
            assert key == f'Карточка {i + 1}'
        assert len(self.player.cards.keys()) == amount

    def test_barrel_check(self):
        barrel = [i for i in range(1, 91)]
        self.player.app_cards()
        for i in barrel:
            assert self.player.barrel_check(i) \
                if i in self.player.only_numbers[0] else \
                not self.player.barrel_check(i)

    def test_game_check(self):
        # Тест.
        self.player.app_cards()
        assert not self.player.game_check()
        # Тест.
        barrel = [i for i in range(1, 91)]
        for i in barrel:
            if i in self.player.only_numbers[0]:
                self.player.barrel_check(i, del_number=True)
        assert self.player.game_check()

    def test_contains(self):
        self.player.app_cards()
        number = []
        barrel = [i for i in range(1, 91)]
        for i in barrel:
            if i not in self.player.only_numbers[0]:
                number.append(i)
                break
        number.append(self.player.only_numbers[0][0])
        assert not number[0] in self.player
        assert number[1] in self.player

    def test_ge(self):
        self.player.app_cards()
        self.second_player = Player()
        self.second_player.app_cards()
        assert self.player >= self.second_player
        self.player.barrel_check(self.player.only_numbers[0][0],
                                 del_number=True)
        assert self.player <= self.second_player

    def test_eq(self):
        self.player.app_cards()
        self.second_player = Player()
        self.second_player.app_cards()
        assert self.player == self.second_player
        self.player.barrel_check(self.player.only_numbers[0][0],
                                 del_number=True)
        assert self.player != self.second_player

    def test_len(self):
        self.player.app_cards()
        assert len(self.player) == 15
        self.player.barrel_check(self.player.only_numbers[0][0],
                                 del_number=True)
        assert len(self.player) == 14
        self.player.barrel_check(self.player.only_numbers[0][1],
                                 del_number=True)
        assert len(self.player) == 13


def test_add_player():
    player = add_player(player_number=1, amount=1, player_type=False)
    assert player.name == 'Игрок 1 Компьютер'
    assert isinstance(player.cards, dict)
    assert len(player.cards) == 1
    player = add_player(player_number=1, amount=1, player_type=True)
    assert player.name == 'Игрок 1 Человек'


def test_step_player():
    """
    answer='n', а move есть в карточке - False;
    answer='n', а move нет в карточке - True;
    answer='y', а move есть в карточке - True;
    answer='y', а move нет в карточке - False;
    :return: False or True
    """
    player = add_player(player_number=1, amount=1, player_type=False)
    barrel = [i for i in range(1, 91)]
    is_on_card = player.only_numbers[0]
    not_on_card = [i for i in barrel if i not in is_on_card][:15]
    for val in is_on_card:
        assert not step_player(player, val, answer='n')
        assert step_player(player, val, answer='y')
    for val in not_on_card:
        assert not step_player(player, val, answer='y')
        assert step_player(player, val, answer='n')


def test_auto_check():
    player = add_player(player_number=1, amount=1, player_type=False)
    assert auto_check(player, 1) is None
