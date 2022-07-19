from classes import PlayingCard, Player
from main_loto import add_player, step_player, auto_check


class TestPlayingCard:

    def setup(self):
        self.card = PlayingCard()

    def test_init(self):
        assert self.card.numbers == []
        assert self.card.linked_lists == []

    def test_filling(self):
        self.card.filling()
        assert len(self.card.numbers) == 3
        assert len(self.card.numbers[0]) == 9
        assert len(self.card.numbers[1]) == 9
        assert len(self.card.numbers[2]) == 9
        assert self.card.numbers[0].count('_') == 4
        assert self.card.numbers[1].count('_') == 4
        assert self.card.numbers[2].count('_') == 4
        # Тест.
        for numbers in self.card.numbers:
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

    def test_app_cards(self):
        # Тест.
        amount = 1
        self.player.app_cards(amount=amount)
        assert len(self.player.cards) == amount
        for i, key in enumerate(self.player.cards.keys()):
            assert key == f'Карточка {i+1}'
        # Тест.
        barrel = [i for i in range(1, 91)]
        result = []
        for card in self.player.cards.values():
            for val in card.numbers:
                for num in val:
                    result.append(True if num in barrel else False)
        assert result.count(True) == 15
        # Тест.
        amount = 5
        self.player.app_cards(amount=amount)
        assert len(self.player.cards) == amount
        for i, key in enumerate(self.player.cards.keys()):
            assert key == f'Карточка {i+1}'
        assert len(self.player.cards.keys()) == amount

    def test_barrel_check(self):
        barrel = [i for i in range(1, 91)]
        self.player.app_cards()
        values = []
        for key in self.player.cards.keys():
            values = self.player.cards[key].linked_lists
        for i in barrel:
            assert self.player.barrel_check(i) if i in values else\
                not self.player.barrel_check(i)

    def test_game_check(self):
        # Тест.
        self.player.app_cards()
        assert not self.player.game_check()
        # Тест.
        barrel = [i for i in range(1, 91)]
        values = []
        for key in self.player.cards.keys():
            values = self.player.cards[key].linked_lists
        for i in barrel:
            if i in values:
                self.player.barrel_check(i, del_number=True)
        assert self.player.game_check()


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
    is_on_card = []
    for key in player.cards.keys():
        is_on_card = player.cards[key].linked_lists
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
