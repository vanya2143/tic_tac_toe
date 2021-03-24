from random import choice

from .area import GameArea
from .exceptions import GameException
from .weapon import Tic, Tac
from .utils import find_winner_combination


class Game:
    """
    Class for creation Game object.

    This is the main class for creating the Tic-Tac-Toe game.
    To work with this class, you need to create a client application like app.py.
    """

    def __init__(self, player1, player2):
        self._weapons = [Tic(), Tac()]
        self._player1 = player1
        self._player2 = player2
        self._free_moves = 9
        self.__find_winner = find_winner_combination
        self._game_area = None
        self._last_move = None

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
        return self._free_moves

    def start_game(self):
        self._game_area = GameArea()

    def _check_winner(self):
        return self.__find_winner(self.show_game_table())

    def set_move(self, player_obj, row, column):
        """
        Method for completing the turn process and checking the player's turn.
        """

        if self._free_moves == 0:
            return GameException('No free moves')

        if player_obj == self._last_move:
            raise GameException('This player has just made a move')

        self._game_area.set_player_move(row, column, self.weapons.get(player_obj))
        winner = self._check_winner()

        if winner:
            return winner
        else:
            self._last_move = player_obj

            # Set player flag
            self.first_player_index = 0 if self.first_player_index else 1
            self._free_moves -= 1

            return False

    def __repr__(self):
        return f'<Game: {self._player1.nickname} ({self.weapons.get(self._player1)}) vs' \
               f' {self._player2.nickname} ({self.weapons.get(self._player2)})>'

    def __str__(self):
        return f'{self._player1.nickname} vs {self._player2.nickname}'
