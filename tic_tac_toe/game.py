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
        self.players = list(self.weapons)
        self.first_player = choice(self.players)
        self.first_player_index = self.players.index(self.first_player)

    def get_current_player(self):
        return self.players[self.first_player_index]

    @property
    def show_game_table(self):
        return self._game_area.show_game_table

    def start_game(self):
        self._game_area = GameArea()
        return self.players, self.first_player

    def move(self, player_obj, x, y):
        if player_obj == self._last_move:
            raise GameException('This player has just made a move')

        self._game_area.player_move(x, y, self.weapons.get(player_obj))
        winner = self._game_area.check_winner()

        if winner:
            return player_obj, winner
        else:
            self._last_move = player_obj

            # Current player flag
            if self.first_player_index:
                self.first_player_index = 0
            else:
                self.first_player_index = 1

            return player_obj, False

    def __str__(self):
        return f'{self._player1.nickname} vs {self._player2.nickname}'

    def __repr__(self):
        return f'<Game: {self._player1.nickname} ({self.weapons.get(self._player1)}) vs {self._player2.nickname} ({self.weapons.get(self._player2)})>'
