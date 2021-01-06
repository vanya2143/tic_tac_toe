from .weapon import Empty
from .utils import ref_data, finder


class GameAreaException(Exception):
    pass


class GameAreaUnitException(GameAreaException):
    pass


class GameAreaIndexException(GameAreaException):
    pass


class GameArea:
    _free_moves = 9

    def __init__(self, game_table_size=3):
        self._empty_obj = Empty()
        self._game_table_size = game_table_size
        self._game_table = self.create_area(self._empty_obj, self._game_table_size)

    @staticmethod
    def create_area(item_obj, size):
        area = []
        for i in range(size):
            area.append([item_obj] * size)
        return area

    @property
    def show_game_table(self):
        return self._game_table

    @property
    def free_moves(self):
        return self._free_moves

    def player_move(self, x, y, value):
        if x > self._game_table_size or self._game_table_size < y:
            raise GameAreaIndexException('Game area index out of range')
        if self._free_moves:
            if self._game_table[x][y]:
                raise GameAreaUnitException('Unit not empty')

            self._game_table[x][y] = value
            self._free_moves -= 1
        else:
            raise GameAreaException('Free moves 0')

    def check_winner(self):
        return finder(self.show_game_table, ref_data)

    def __repr__(self):
        return f'<Game area {self._game_table}>'

    def __str__(self):
        return '\n'.join('\t'.join(i.name for i in row) for row in self.show_game_table)
