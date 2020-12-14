# TODO Запрет на смену оружия во время игры
# TODO Переделать _game_table
# TODO Проверка победителя
# TODO Проверка выиграшных комбинацый

from random import choice

from .area import GameArea
from .player import Player
from .weapon import Tic, Toc


# TODO Game table будет отдельным объектом
class Game:
    _weapons = [Tic(), Toc()]
    _game_table = None
    _last_move = None

    def __init__(self, player1, player2):
        self._player1 = player1
        self._player2 = player2

        self.weapons = {
            self._player1: self._weapons.pop(choice(range(2))),
            self._player2: self._weapons.pop()
        }

    def show_game_table(self):
        return self._game_table

    def check_winner(self):
        pass

    def start_game(self):
        self._game_table = GameArea()

    def move(self, player_obj, *weapon_position):
        pass

    def __repr__(self):
        return f'<Game: {self._player1.get_nickname} vs {self._player2.get_nickname}>'



