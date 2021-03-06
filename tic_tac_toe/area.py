from .weapon import Empty, Weapon


class GameAreaException(Exception):
    pass


class GameAreaUnitException(GameAreaException):
    pass


class GameAreaIndexException(GameAreaException):
    pass


class GameArea:
    """
    Class for create GameArea object.

    """
    def __init__(self):
        self._empty_obj = Empty()
        self._size = 3
        self._free_moves = 9
        self._game_table = self.__create_game_table(self._empty_obj, self._size)

    @property
    def show_game_table(self):
        return self._game_table

    @property
    def free_moves(self):
        return self._free_moves

    def player_move(self, row: int, column: int, value: Weapon) -> None:
        """ Class method for completing the move process and check player move. """

        if row >= self._size or self._size <= column:
            raise GameAreaIndexException('Game area index out of range')
        if self._free_moves:
            if self._game_table[row][column]:
                raise GameAreaUnitException('Unit not empty')

            self._game_table[row][column] = value
            self._free_moves -= 1
        else:
            raise GameAreaException('Free moves 0')

    @staticmethod
    def __create_game_table(item_obj, size):
        area = []
        for i in range(size):
            area.append([item_obj] * size)
        return area

    def __repr__(self):
        return f'<Game area {self._game_table}>'

    def __str__(self):
        return '\n'.join('\t'.join(i.name for i in row) for row in self.show_game_table)
