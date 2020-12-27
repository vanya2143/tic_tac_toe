# TODO Запрет на смену оружия во время игры
# TODO Переделать _game_table
# TODO Проверка победителя
# TODO Проверка выигранных комбинаций

from random import choice

from .area import GameArea
from .weapon import Tic, Tac


# TODO Game table будет отдельным объектом
class Game:
    _game_area = None
    _last_move = None

    def __init__(self, player1, player2):
        self._weapons = [Tic(), Tac()]
        self._player1 = player1
        self._player2 = player2

        self.weapons = {
            self._player1: self._weapons.pop(choice(range(2))),
            self._player2: self._weapons.pop()
        }

    def show_game_table(self):
        return self._game_area

    def start_game(self):
        self._game_area = GameArea()

    def move(self, player_obj, x, y):
        if player_obj != self._last_move:
            m = self._game_area.player_move(x, y, self.weapons.get(player_obj))

            self._last_move = player_obj

            if m:
                return f'Winner {m}', self._game_area
            else:
                return 0, self._game_area

        else:
            return f'Now not your move, please wait!'

    def __str__(self):
        return f'{self._player1.nickname} vs {self._player2.nickname}'

    def __repr__(self):
        return f'<Game: {self._player1.nickname} vs {self._player2.nickname}>'
