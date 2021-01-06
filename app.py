import os
import sys

from tic_tac_toe.game import Game, GameException
from tic_tac_toe.player import Player
from tic_tac_toe.area import GameAreaUnitException, GameAreaIndexException
from tic_tac_toe.weapon import Weapon
from tic_tac_toe.utils import Colors


# TODO Добавить отображение сообжений

def clean_area():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')


def draw_game_table(game_table: list):
    game_t = [['#', '0', '1', '2'], ['0'], ['1'], ['2']]
    colorize_staff(game_t)

    for index, row in enumerate(game_table, 1):
        game_t[index].extend(row)

    return '\n'.join('  '.join(i.name if issubclass(type(i), Weapon) else i for i in row) for row in game_t)


def to_green(item):
    return f'{Colors.OKGREEN}{item}{Colors.ENDC}'


def colorize_staff(seq):
    for r_index, row in enumerate(seq):
        for el_index, elem in enumerate(row):
            item = elem
            seq[r_index][el_index] = f'{Colors.SILVER}{item}{Colors.ENDC}'


def colorize(game_table, win_array: tuple):
    for row in win_array:
        item = game_table[row[0]][row[1]]
        game_table[row[0]][row[1]] = to_green(item.name)

    return game_table


def draw(game_obj, last_moved, with_color=False, win=None):
    clean_area()
    print(messages)
    print(game_obj, f'\nLast move: {last_moved[0]} - {last_moved[1]}')
    if with_color:
        print(draw_game_table(colorize(game_obj.show_game_table(), win)))
    else:
        print(draw_game_table(game_obj.show_game_table()))


player1 = input('Enter player1 name: ')
player2 = input('Enter player2 name: ')

p1 = Player(str(player1))
p2 = Player(str(player2))

# p1 = Player('Player1')
# p2 = Player('Player2')

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
        game.start_game()

        last_move = ['', '']
        winner = False
        messages = []

        # Game loop
        while True:
            player = game.get_current_player()
            # Draw game
            draw(game, last_move)

            # If free moves is 0
            if not game.free_moves():
                draw(game, last_move)
                print('No free moves')

                question = input('\nTry again? y/[n] ')
                if question == 'n':
                    game_flag = False
                    break
                elif question == 'y':
                    break
                else:
                    game_flag = False
                    break

            string = f'{player.nickname} is moving, weapon: {game.weapons.get(player).name} --> : '
            game_action = input(string)

            if game_action == 'Q':
                sys.exit(0)
            elif game_action == 'q':
                break

            try:
                user_action = tuple(map(int, game_action.split(',')))
            except ValueError:
                messages.append('Use integers with coma separate: 1,1')
                continue

            # Actions
            try:
                moved_player, winner = game.move(player, *user_action)
                last_move = moved_player.nickname, user_action
            except GameAreaUnitException:
                messages.append('This unit not empty!')
                continue
            except GameAreaIndexException:
                continue
            except GameException as e:
                print(e)

            # If player win
            if winner:
                draw(game, last_move, True, winner[1])
                print(f'Winner {moved_player.nickname}, weapon {winner[0].name}')

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

# if __name__ == '__main__':
#     pass
