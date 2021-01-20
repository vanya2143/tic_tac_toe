import os
import sys

from tic_tac_toe.game import Game, GameException
from tic_tac_toe.player import Player
from tic_tac_toe.area import GameAreaUnitException, GameAreaIndexException
from tic_tac_toe.weapon import Weapon
from tic_tac_toe.utils import Colors


# TODO Добавить отображение сообщений

def clean_area():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')


# Add staff data to game table
def create_game_map(game_table: list):
    game_t = [['#', '0', '1', '2'], ['0'], ['1'], ['2']]
    set_game_style(game_t)

    for index, row in enumerate(game_table, 1):
        game_t[index].extend(row)

    return '\n'.join('  '.join(i.name if issubclass(type(i), Weapon) else i for i in row) for row in game_t)


def set_game_style(seq):
    for r_index, row in enumerate(seq):
        for el_index, elem in enumerate(row):
            item = elem
            seq[r_index][el_index] = f'{Colors.bold(item)}'


# Set color for win items
def colorize(game_table, win_array: tuple):
    for row in win_array:
        item = game_table[row[0]][row[1]]
        game_table[row[0]][row[1]] = Colors.to_green(item.name)

    return game_table


# Show game
def draw(game_obj, last_moved, with_color=False, win=None):
    clean_area()

    last_player = last_moved[0]
    player_move = last_moved[1]

    print(f'{Colors.underline(game_obj)}', f'\nLast move: {last_player} - {player_move}')

    # If we have a winner we use colorize()
    if with_color:
        print(create_game_map(colorize(game_obj.show_game_table(), win)))
    else:
        print(create_game_map(game_obj.show_game_table()))


def context_menu():
    # Context menu
    question = input('\nTry again? y/[n] ')
    if question == 'y':
        return True
    else:
        return False


# player1 = input('Enter player1 name: ')
# player2 = input('Enter player2 name: ')
#
# p1 = Player(str(player1))
# p2 = Player(str(player2))

p1 = Player('Player1')
p2 = Player('Player2')

print('')
print('s to start game')
print('q exit')

action = str(input('---> '))

if action == 'q':
    sys.exit(0)

if action == 's':
    # Game session loop
    game_session_flag = True
    while game_session_flag:
        # Init game
        game = Game(p1, p2)
        game.start_game()

        last_move = ['', '']
        winner = False
        messages = []
        current_game_flag = True

        # Current game loop
        while current_game_flag:
            player = game.get_current_player()
            # Draw game
            draw(game, last_move)

            # If free moves is 0
            if not game.free_moves():
                draw(game, last_move)
                print('No free moves')

                # Context menu
                # question = input('\nTry again? y/[n] ')
                # if question == 'y':
                #     break
                # else:
                #     game_session_flag = False
                #     break
                game_session_flag = context_menu()
                break

            # TODO Система уведомлений
            print()
            if messages:
                print(f'{Colors.reverse(messages.pop())}')
                messages.clear()

            string = f'{Colors.bold(player.nickname)} is moving, weapon: ' \
                     f'{Colors.bold(game.weapons.get(player).name)} (row,column) \n--> '

            game_action = input(string)

            if game_action == 'Q':
                sys.exit(0)
            elif game_action == 'q':
                break

            # Parse user input
            try:
                user_action = tuple(map(int, game_action.split(',')))
            except ValueError:
                messages.append('Use integers with coma separate: row,column')
                continue

            # Actions
            try:
                moved_player, winner = game.move(player, *user_action)
                last_move = moved_player.nickname, game_action
            except GameAreaUnitException:
                messages.append('This unit not empty!')
                continue

            # If player win
            if winner:
                draw(game, last_move, True, winner[1])
                print(f'Winner {moved_player.nickname}, weapon {winner[0].name}')

                # Context menu
                # question = input('\nTry again? y/[n] ')
                # if question == 'y':
                #     break
                # else:
                #     game_session_flag = False
                #     break

                game_session_flag = context_menu()
                break

            print(f'{"*" * 20}\n\n')
