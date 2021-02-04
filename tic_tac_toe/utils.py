ref_data = (
    # rows
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),

    # cols
    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),

    # X
    ((0, 0), (1, 1), (2, 2)),
    ((0, 2), (1, 1), (2, 0)),
)


class Colors:
    OKGREEN = '\u001b[38;5;82m'
    ENDC = '\u001b[0m'
    WHITE = '\u001b[38;5;255m'
    SILVER = '\u001b[38;5;249m'

    B_STYLE_BOLD = '\u001b[1m'
    STYLE_REVERSED = '\u001b[7m'
    STYLE_UNDERLINE = '\u001b[4m'

    @classmethod
    def to_green(cls, item):
        return f'{cls.OKGREEN}{item}{cls.ENDC}'

    @classmethod
    def bold(cls, item):
        return f'{cls.B_STYLE_BOLD}{item}{cls.ENDC}'

    @classmethod
    def underline(cls, item):
        return f'{cls.STYLE_UNDERLINE}{item}{cls.ENDC}'

    @classmethod
    def reverse(cls, item):
        return f'{cls.STYLE_REVERSED}{item}{cls.ENDC}'


def finder(game_table: list, r_data: tuple):
    for elem in r_data:
        tmp_list = []
        for addr in elem:
            tmp_list.append(game_table[addr[0]][addr[1]])

        # Если все ячейки не пусты
        if all(tmp_list):
            # Если во всех трех ячейках одинаковый элемент
            row_set = set(tmp_list)
            if len(row_set) == 1:
                return row_set.pop(), elem
