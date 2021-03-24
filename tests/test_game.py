import pytest

from tic_tac_toe.game import Game
from tic_tac_toe.exceptions import GameException
from tic_tac_toe.player import Player


# Initial players objects
@pytest.fixture(scope='module')
def player_obj():
    return Player('Player1'), Player('Player2')


# Initial game object
@pytest.fixture(scope='module')
def game_obj(player_obj):
    return Game(*player_obj)


@pytest.mark.game_positive_mark
def test_start_game(game_obj):
    game_obj.start_game()
    assert game_obj._game_area is not None
    assert str(game_obj) == 'Player1 vs Player2'


@pytest.mark.game_positive_mark
def test_players(game_obj):
    assert game_obj._player1.nickname == 'Player1'
    assert game_obj._player2.nickname == 'Player2'


@pytest.mark.game_positive_mark
def test_player_move(game_obj):
    player = game_obj.first_player
    assert game_obj.set_move(player, 0, 0) is False
    assert game_obj.free_moves() == 8


@pytest.mark.game_negative_mark
@pytest.mark.xfail(reason='This player has just made a move', raises=GameException)
def test_player_move_exception(game_obj):
    player = game_obj.players[0 if game_obj.first_player_index else 1]
    assert game_obj.set_move(player, 1, 1) == GameException


@pytest.mark.game_positive_mark
def test_win(player_obj):
    game = Game(*player_obj)
    game.start_game()

    assert game.set_move(game.get_current_player(), 0, 0) is False
    assert game.set_move(game.get_current_player(), 1, 0) is False
    assert game.set_move(game.get_current_player(), 1, 1) is False
    assert game.set_move(game.get_current_player(), 2, 0) is False
    assert game.set_move(game.get_current_player(), 2, 2) is not False
