import os
import sys
from random import choice
from copy import deepcopy

from tic_tac_toe.game import Game, GameException
from tic_tac_toe.player import Player
from tic_tac_toe.area import GameAreaUnitException, GameAreaException
from tic_tac_toe.weapon import Colors, Empty


def clean_area():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')


def draw_area(game_table: list):
    game_t = [['#', '0', '1', '2'], ['0'], ['1'], ['2']]

    for index, row in enumerate(game_table, 1):
        game_t[index].extend(row)

    return '\n'.join('  '.join(i.name if isinstance(i, Empty) else i for i in row) for row in game_t)


def to_green(item):
    return f'{Colors.OKGREEN}{item}{Colors.ENDC}'


def colorize(game_table, win_array: tuple):
    for row in win_array:
        item = game_table[row[0]][row[1]]
        game_table[row[0]][row[1]] = to_green(item)

    return game_table


# player1 = input('Enter player1 name: ')
# player2 = input('Enter player2 name: ')

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
    game_flag = True
    while game_flag:
        # Init game
        game = Game(p1, p2)
        players, first_player = game.start_game()

        last_move = ['', '']
        winner = False
        messages = []

        # Game loop
        while True:
            player = game.get_current_player()
            # clean_area()

            # Show game area
            print(messages)
            print(game, f'\nLast move: {last_move[0]} - {last_move[1]}')
            print(draw_area(game.show_game_table))

            string = f'{player.nickname} is moving, weapon: {game.weapons.get(player)} --> : '
            game_action = input(string)

            if game_action == 'Q':
                sys.exit(0)
            elif game_action == 'q':
                break

            print(game_action)
            user_action = tuple(map(int, game_action.split(',')))

            # Actions
            try:
                moved_player, winner = game.move(player, *user_action)
                last_move = moved_player.nickname, user_action
            except GameAreaUnitException:
                messages.append('This unit not empty!')
                print('This unit not empty!')
                continue
            except GameAreaException:
                print('Out of game area range')
                continue
            except GameException as e:
                print(e)

            if winner:
                clean_area()
                print(messages)
                print(game, f'\nLast move: {last_move[0]} - {last_move[1]}')
                print(f'Winner {moved_player.nickname}, weapon {winner[0]}')
                gt = game.show_game_table
                print(draw_area(colorize(gt, winner[1])))

                question = input('\nTry again? y/[n] ')
                if question == 'n':
                    game_flag = False
                    break
                elif question == 'y':
                    break
                else:
                    game_flag = False
                    break

            print(f'{"*" * 20}\n\n')
