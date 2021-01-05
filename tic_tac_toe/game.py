# TODO Запрет на смену оружия во время игры
# TODO Переделать _game_table
# TODO Проверка победителя
# TODO Проверка выигранных комбинаций

from random import choice

from .area import GameArea, GameAreaException, GameAreaUnitException
from .weapon import Tic, Tac


class GameException(Exception):
    pass


class Game:
    _game_area = None
    _last_move = None

    def __init__(self, player1, player2):
        self._weapons = ['x', 'o']
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
        if player_obj == self._last_move:
            raise GameException('This player already moved')

        self._game_area.player_move(x, y, self.weapons.get(player_obj))
        winner = self._game_area.check_winner()
        if winner:
            return winner
        else:
            self._last_move = player_obj

    def __str__(self):
        return f'{self._player1.nickname} vs {self._player2.nickname}'

    def __repr__(self):
        return f'<Game: {self._player1.nickname} vs {self._player2.nickname}>'
