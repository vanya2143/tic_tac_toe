from .weapon import Empty


# Возвращаем выиграшный елемент если он есть иначе False
def is_elem(seq: list):
    elem = set(seq)
    return elem.pop() if len(elem) == 1 else False


# Транспонируем матрицу
def transpose(seq: list):
    return [
        [item[i] for item in seq] for i in range(len(seq[0]))
    ]


# Переворачиваем строку
def reverse_row(seq: list):
    return [row[::-1] for row in seq]


# Находим выиграшный елемент в таблице
def find_win_row(checked_seq: list, t=False):
    if any(checked_seq):
        for index, elem in enumerate(checked_seq):
            if elem:
                return t, index, elem
    return False


# Находим выиграшную позицию в таблице если t=True переворачиваем
def check_table(table: list, t: bool = False):
    data = transpose(table) if t else table
    rows = find_win_row([is_elem(row) for row in data], t)
    if rows:
        return rows
    data = reverse_row(table) if t else table
    d = 'right' if t else 'left'  # slash or backslash
    diagonal = t, d, is_elem([row[1][row[0]] for row in enumerate(data)])
    if diagonal[2]:
        return diagonal

    return False


# Проверяем таблицу на выигрыш
def check_game_table(game_table: list):
    origin_table = check_table(game_table)
    if origin_table:
        return origin_table
    else:
        transposed_table = check_table(game_table, t=True)
        return transposed_table


class GameAreaException(Exception):
    pass


class GameArea:
    _values = 'xo'
    # TODO Проверять кол-во возможных ходов
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
    def game_table(self):
        return self._game_table

    def player_move(self, x, y, value):
        # TODO Проверка хода
        if self._game_table[x][y]:
            raise GameAreaException('Unit not empty')

        self._game_table[x][y] = value
        self._check_winner()

        return self._check_winner()

    def _check_winner(self):
        # TODO Возвращать адреса выиграшных позиций
        win_position = check_game_table(self.game_table)  # (True, 1, 'x')

        if win_position:
            return win_position

        # if win_position:
        #     transposed, index, elem = win_position
        #     print(win_position)
        #     position = 'col' if transposed else 'row'
        #
        #     # Разукрасить выиграшную позицию
        #     print('\n'.join('\t'.join(row) for row in self.game_table))
        #
        #     if type(index) == int:
        #         return f'Winner {elem}: {position}: {index}'
        #     else:
        #         return f'Winner {elem}: {index}'

    def __repr__(self):
        return f'<Game area {self._game_table}>'

    def __str__(self):
        return '\n'.join('\t'.join(i.name for i in row) for row in self.game_table)
