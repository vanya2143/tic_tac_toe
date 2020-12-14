import pytest

from src.tic_tac_toe.game import Game
from src.tic_tac_toe.player import Player


@pytest.fixture(scope='module', autouse=True)
def create_player1_obj():
    return Player('Vano')


@pytest.fixture(scope='module', autouse=True)
def create_player2_obj():
    return Player('Oleg')


@pytest.fixture(scope='module', autouse=True)
def create_game_obj(create_player1_obj, create_player2_obj):
    return Game(create_player1_obj, create_player2_obj)


def test_start_game(create_game_obj):
    create_game_obj.start_game()

    assert isinstance(create_game_obj._player1, Player)
    assert create_game_obj._player1.get_nickname == 'Vano'
