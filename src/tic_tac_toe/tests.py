_game_table_1 = [['x', 'x', 'x'],
                 ['', '', ''],
                 ['', '', '']]

_game_table_2 = [['', '', ''],
                 ['x', 'x', 'x'],
                 ['', '', '']]

_game_table_3 = [['', '', ''],
                 ['', '', ''],
                 ['x', 'x', 'x']]

_game_table_4 = [['x', '', ''],
                 ['x', '', ''],
                 ['x', '', '']]

_game_table_5 = [['', 'x', ''],
                 ['', 'x', ''],
                 ['', 'x', '']]

_game_table_6 = [['', '', 'x'],
                 ['', '', 'x'],
                 ['', '', 'x']]

_game_table_7 = [['x', '', ''],
                 ['', 'x', ''],
                 ['', '', 'x']]

_game_table_8 = [['', '', 'x'],
                 ['', 'x', ''],
                 ['x', '', '']]

_game_table_9 = [['', '', 'x'],
                 ['', '', ''],
                 ['x', '', '']]

# print('1', check_game_table(_game_table_1))
# print('2', check_game_table(_game_table_2))
# print('3', check_game_table(_game_table_3))
# print('4', check_game_table(_game_table_4))
# print('5', check_game_table(_game_table_5))
# print('6', check_game_table(_game_table_6))
# print('7', check_game_table(_game_table_7))
# print('8', check_game_table(_game_table_8))
# print('8', check_game_table(_game_table_9))
# print(find_winner_position(_game_table_1))

import os
print(os.getcwd())
path = os.environ['PYTHONPATH']
os.environ['PYTHONPATH'] = path + ';' + os.getcwd()
print(os.environ['PYTHONPATH'])
