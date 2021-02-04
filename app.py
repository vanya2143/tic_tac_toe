import os
import sys

from tic_tac_toe.game import Game
from tic_tac_toe.player import Player
from tic_tac_toe.area import GameAreaUnitException, GameAreaIndexException
from tic_tac_toe.weapon import Staff
from tic_tac_toe.utils import Colors


def clean_area():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')


# Add staff data to game table
def create_game_map(game_table: list):
    game_t = [
        [Staff('#'), Staff('0'), Staff('1'), Staff('2')],
        [Staff('0')],
        [Staff('1')],
        [Staff('2')]
    ]

    for index, row in enumerate(game_table, 1):
        game_t[index].extend(row)

    # If we have a winner his weapon object will be replaced to string because I wont to show it in green :)
    return '\n'.join('  '.join(i if isinstance(i, str) else i.name for i in row) for row in game_t)


# Set color for win items
def colorize(game_table, win_array: tuple):
    for row in win_array:
        item = game_table[row[0]][row[1]]
        game_table[row[0]][row[1]] = Colors.to_green(item.name)

    return game_table


# Show game
def draw_frame(game_obj, last_moved, _win_obj, msg_tray):
    _last_player = last_moved[0]
    _coordinates = last_moved[1]

    clean_area()
    print(f'{Colors.underline(game_obj)}', f'\nLast move: {_last_player} - {_coordinates}')

    # If we have a winner we use colorize()
    if _win_obj:
        print(create_game_map(colorize(game_obj.show_game_table(), _win_obj[1])), end='\n\n')
        print(f'Winner {player.nickname}, weapon {_win_obj[0].name}')
        _game_flag = context_menu()
        return _game_flag
    else:
        print(create_game_map(game_obj.show_game_table()), end='\n\n')

    if not game_obj.free_moves():
        print(f'{Colors.reverse("No free moves")}')
        return context_menu()

    if msg_tray:
        print(f'{Colors.reverse(messages.pop())}')
        messages.clear()


# Show question after game
def context_menu():
    question = input('\nTry again? y/[n] ')
    if question == 'y':
        return True
    else:
        return False


# p1 = Player('Player1')
# p2 = Player('Player2')

print(f'  Welcome to\n Tic Tac Toe')
print()
print('press "s" to start game')
print('press "q" or "enter" key to exit')

try:
    action = str(input('---> '))
except (EOFError, KeyboardInterrupt):
    print('Bye!')
    sys.exit(0)

if action == 'q':
    sys.exit(0)

if action == 's':
    player1 = input('Enter player1 name: ')
    player2 = input('Enter player2 name: ')

    p1 = Player(str(player1))
    p2 = Player(str(player2))

    # Game session loop
    game_session_flag = True

    while game_session_flag:
        # Init game
        game = Game(p1, p2)
        game.start_game()

        # Current game data
        last_move = ['', '']
        winner = False
        messages = []
        current_game_flag = True

        # Current game loop
        while current_game_flag:
            # Show current game
            flag = draw_frame(game, last_move, winner, messages)  # -> Bool
            if flag:
                break
            elif not flag and flag is not None:
                print('Bye!')
                sys.exit(0)

            player = game.get_current_player()
            string = f'{Colors.bold(player.nickname)} is moving, weapon: ' \
                     f'{Colors.bold(game.weapons.get(player).name)} (row,column) \n--> '

            try:
                input_coordinates = input(string)
            except (EOFError, KeyboardInterrupt):
                print('Bye!')
                sys.exit(0)

            # Restart game
            if input_coordinates == 'r':
                break

            # Parse input coordinates
            try:
                coordinates = tuple(map(int, input_coordinates.split(',')))
            except ValueError:
                messages.append('Use integers with coma separate: row,column')
                continue

            # Submit users coordinates
            try:
                winner = game.move(player, *coordinates)  # -> Union[Tuple[list, Any], bool
                last_move = player.nickname, input_coordinates

            except GameAreaUnitException:
                messages.append('This unit is not empty!')
                continue

            except GameAreaIndexException:
                messages.append('You has input a non-existent address.')
                continue

            except TypeError as e:
                error = e.args[0].split(" ")[-1]
                msg = f'You forgot to provide one argument {error}'
                messages.append(msg)
                continue
