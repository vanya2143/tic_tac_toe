import pytest

from tic_tac_toe.area import GameArea
from tic_tac_toe.area import GameAreaException
from tic_tac_toe.weapon import Empty, Tic, Tac
from tic_tac_toe.utils import ref_data


# Initial area object
@pytest.fixture(scope='module')
def game_area_obj():
    return GameArea()


@pytest.mark.area_positive_mark
def test_game_table(game_area_obj):
    assert isinstance(game_area_obj.game_table[0][0], Empty)


# Test move
@pytest.mark.area_positive_mark
def test_move(game_area_obj):
    _ = game_area_obj.player_move(0, 0, 'x')
    _ = game_area_obj.player_move(1, 1, 'o')
    _ = game_area_obj.player_move(2, 2, 'x')

    assert game_area_obj.game_table[0][0] == 'x'
    assert game_area_obj.game_table[1][1] == 'o'
    assert game_area_obj.game_table[2][2] == 'x'


@pytest.mark.area_negative_mark
@pytest.mark.xfail(reason='This unit does not empty!', raises=GameAreaException)
def test_move_fail_not_empty():
    ga = GameArea()
    tic = Tic()
    ga.player_move(0, 0, tic)

    assert ga.player_move(0, 0, tic) == GameAreaException


# TODO Уедет в тесты игрового движка
@pytest.mark.area_negative_mark
@pytest.mark.xfail(reason='This weapon does not allowed!', raises=GameAreaException)
def test_move_fail_allowed_weapon(game_area_obj):
    pass


@pytest.mark.area_negative_mark
@pytest.mark.xfail(reason='Game area index out of range', raises=GameAreaException)
def test_move_fail_out_of_range(game_area_obj):
    assert game_area_obj.player_move(10, 10, 'x') == GameAreaException


# Check winner combinations
@pytest.mark.area_positive_mark
def test_check_winner():
    for moves in ref_data:
        ga = GameArea()
        for cur_move, move in enumerate(moves):
            ga.player_move(move[0], move[1], 'x')
            if cur_move == 2:
                assert ga.check_winner() == ('x', moves)
