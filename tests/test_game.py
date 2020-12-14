import pytest

from src.tic_tac_toe.game import Game
from src.tic_tac_toe.player import Player


# Initial player1 object
@pytest.fixture(scope='module')
def player1_obj():
    return Player('Vano')


# Initial player1 object
@pytest.fixture(scope='module')
def player2_obj():
    return Player('Oleg')


# Initial game object
@pytest.fixture(scope='module')
def game_obj(player1_obj, player2_obj):
    return Game(player1_obj, player2_obj)


def test_start_game(game_obj):
    game_obj.start_game()
    assert game_obj._game_table is not None


def test_players(game_obj):
    assert game_obj._player1.nickname == 'Vano'
    assert game_obj._player2.nickname == 'Oleg'
