import os
import sys
from random import choice

from tic_tac_toe.game import Game
from tic_tac_toe.player import Player


def clean_area():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')


player1 = input('Enter player1 name: ')
player2 = input('Enter player2 name: ')

p1 = Player(str(player1))
p2 = Player(str(player2))

print('')
print('s to start game')
print('q exit')

action = str(input('--->'))

if action == 'q':
    sys.exit(0)

if action == 's':
    # Game session loop
    game_flag = True
    while game_flag:
        game = Game(p1, p2)
        game.start_game()
        players = [p1, p2]
        first_player = choice(players)
        first_player_index = players.index(first_player)
        last_move = [None, None]

        print(game.show_game_table())

        # Game loop
        while True:
            player = players[first_player_index]
            # clean_area()

            # Show game area
            print(game, f'\nLast move: {last_move[0]} - {last_move[1]}')
            print(game.show_game_table())

            string = f'{player.nickname} can move, your weapon: {game.weapons.get(player)} --> x, y: '
            game_action = input(string)

            if game_action == 'Q':
                sys.exit(0)
            elif game_action == 'q':
                break

            print(game_action)
            user_action = tuple(map(int, game_action.split(',')))

            # Current player flag
            if first_player_index:
                first_player_index = 0
            else:
                first_player_index = 1

            last_move = player, user_action
            move = game.move(player, *user_action)
            if move[0]:
                # clean_area()
                print(game, f'Last move: {last_move[0].nickname} - {last_move[1]}')
                print(game.show_game_table())
                print(f'Winner: {player}, weapon: {game.weapons.get(player)}')

                question = input('Try again? y,n ')
                if question == 'n':
                    game_flag = False
                    break
                elif question == 'y':
                    break
