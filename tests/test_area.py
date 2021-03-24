import pytest

from tic_tac_toe.area import GameArea
from tic_tac_toe.exceptions import GameAreaException
from tic_tac_toe.weapon import Empty, Tic, Tac


# Initial area object
@pytest.fixture(scope='module')
def game_area_obj():
    return GameArea()


@pytest.mark.area_positive_mark
def test_game_table(game_area_obj):
    assert isinstance(game_area_obj.show_game_table[0][0], Empty)


# Test move
@pytest.mark.area_positive_mark
def test_move(game_area_obj):
    _ = game_area_obj.set_player_move(0, 0, 'x')
    _ = game_area_obj.set_player_move(1, 1, 'o')
    _ = game_area_obj.set_player_move(2, 2, 'x')

    assert game_area_obj.show_game_table[0][0] == 'x'
    assert game_area_obj.show_game_table[1][1] == 'o'
    assert game_area_obj.show_game_table[2][2] == 'x'


@pytest.mark.area_negative_mark
@pytest.mark.xfail(reason='This unit does not empty!', raises=GameAreaException)
def test_move_fail_not_empty():
    ga = GameArea()
    tic = Tic()
    ga.set_player_move(0, 0, tic)

    assert ga.set_player_move(0, 0, tic) == GameAreaException


@pytest.mark.area_negative_mark
@pytest.mark.xfail(reason='Game area index out of range', raises=GameAreaException)
def test_move_fail_out_of_range(game_area_obj):
    assert game_area_obj.set_player_move(10, 10, 'x') == GameAreaException


@pytest.mark.area_negative_mark
@pytest.mark.xfail(reason='Free moves 0', raises=GameAreaException)
def test_free_moves_exception():
    ga = GameArea()
    for row in range(3):
        for column in range(3):
            ga.set_player_move(row, column, 'x')

    assert ga.set_player_move(1, 1, 'x') == GameAreaException
