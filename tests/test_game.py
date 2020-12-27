import pytest

from tic_tac_toe.game import Game
from tic_tac_toe.player import Player


# Initial players objects
@pytest.fixture(scope='module')
def player_obj():
    return Player('Ivan'), Player('Oleg')


# Initial game object
@pytest.fixture(scope='module')
def game_obj(player_obj):
    return Game(*player_obj)


def test_start_game(game_obj):
    game_obj.start_game()
    assert game_obj._game_area is not None


def test_players(game_obj):
    assert game_obj._player1.nickname == 'Ivan'
    assert game_obj._player2.nickname == 'Oleg'
