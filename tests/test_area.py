import pytest

from tic_tac_toe.area import GameArea
from tic_tac_toe.area import GameAreaException

from tic_tac_toe.weapon import Empty

# Winner combinations
winner_moves = {
    (False, 'left', 'x'): [[0, 0, 'x'], [1, 1, 'x'], [2, 2, 'x']],
    (True, 'right', 'x'): [[0, 2, 'x'], [1, 1, 'x'], [2, 0, 'x']],

    (False, 0, 'x'): [[0, 0, 'x'], [0, 1, 'x'], [0, 2, 'x']],
    (False, 1, 'x'): [[1, 0, 'x'], [1, 1, 'x'], [1, 2, 'x']],
    (False, 2, 'x'): [[2, 0, 'x'], [2, 1, 'x'], [2, 2, 'x']],

    (True, 0, 'x'): [[0, 0, 'x'], [1, 0, 'x'], [2, 0, 'x']],
    (True, 1, 'x'): [[0, 1, 'x'], [1, 1, 'x'], [2, 1, 'x']],
    (True, 2, 'x'): [[0, 2, 'x'], [1, 2, 'x'], [2, 2, 'x']],
}


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
def test_move_fail_not_empty(game_area_obj):
    pass


@pytest.mark.area_negative_mark
@pytest.mark.xfail(reason='This weapon does not allowed!', raises=GameAreaException)
def test_move_fail_allowed_weapon(game_area_obj):
    pass


@pytest.mark.area_negative_mark
@pytest.mark.xfail(reason='This move does not in allowed area range!', raises=GameAreaException)
def test_move_fail_out_of_range(game_area_obj):
    pass


# Check winner combinations
@pytest.mark.area_positive_mark
def test_check_winner():
    for key, moves in winner_moves.items():
        ga = GameArea()
        for cur_move, move in enumerate(moves):
            m = ga.player_move(*move)
            if cur_move == 2:
                assert m == key
