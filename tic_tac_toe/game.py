from random import choice

from .area import GameArea
from .weapon import Tic, Tac
from .utils import find_winner_combination


class GameException(Exception):
    pass


class Game:
    """
    Class for create Game object.

    This is the main class for create a game Tic Tac Toe.
    To work with this class, you need to create a client application,
    for example app.py.
    """
    _game_area = None
    _last_move = None

    def __init__(self, player1, player2):
        self._weapons = [Tic(), Tac()]
        self._player1 = player1
        self._player2 = player2

        # Equipment players of random weapon
        self.weapons = {
            self._player1: self._weapons.pop(choice(range(2))),
            self._player2: self._weapons.pop()
        }
        self.players = list(self.weapons)
        self.first_player = choice(self.players)
        self.first_player_index = self.players.index(self.first_player)

    def get_current_player(self):
        return self.players[self.first_player_index]

    def show_game_table(self):
        return self._game_area.show_game_table

    def free_moves(self):
        return self._game_area.free_moves

    def start_game(self):
        self._game_area = GameArea()

    def check_winner(self):
        return find_winner_combination(self.show_game_table())

    def move(self, player_obj, row, column):
        """ Class method for completing the move process and check player move. """

        if player_obj == self._last_move:
            raise GameException('This player has just made a move')

        self._game_area.player_move(row, column, self.weapons.get(player_obj))
        winner = self.check_winner()

        if winner:
            return winner
        else:
            self._last_move = player_obj

            # Current player flag
            self.first_player_index = 0 if self.first_player_index else 1

            return False

    def __repr__(self):
        return f'<Game: {self._player1.nickname} ({self.weapons.get(self._player1)}) vs' \
               f' {self._player2.nickname} ({self.weapons.get(self._player2)})>'

    def __str__(self):
        return f'{self._player1.nickname} vs {self._player2.nickname}'
