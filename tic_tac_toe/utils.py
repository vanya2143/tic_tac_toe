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

# arr = [
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', ''],
# ]


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
