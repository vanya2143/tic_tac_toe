from .exceptions import GameAreaIndexException
from .exceptions import GameAreaUnitException
from .weapon import Empty, Weapon


class GameArea:
    """
    Class for creation GameArea object.

    """

    def __init__(self):
        self._empty_obj = Empty()
        self._size = 3
        self._game_table = self.__create_game_area(self._empty_obj, self._size)

    @property
    def show_game_table(self):
        return self._game_table

    def set_player_move(self, row: int, column: int, value: Weapon):
        """
        Method for checking the game area for a free unit.

        :param row: row index in game area
        :param column: column index in game area
        :param value: player weapon object
        :return: None
        """

        if row >= self._size or self._size <= column:
            raise GameAreaIndexException('Game area index out of range')
        if self._game_table[row][column]:
            raise GameAreaUnitException('Unit not empty')

        self._game_table[row][column] = value

    @staticmethod
    def __create_game_area(item_obj, size) -> list:
        """
        Method for creating a game area with special size and objects.

        :param item_obj: Empty object
        :param size: size of area
        :return: list of game area
        """
        area = []
        for i in range(size):
            area.append([item_obj] * size)
        return area

    def __repr__(self):
        return f'<Game area {self._game_table}>'

    def __str__(self):
        return '\n'.join('\t'.join(i.name for i in row) for row in self.show_game_table)
