# Main run file
import os
import numpy as np
import game


# create new game
g = game.Game()


# main game loop
while(g.check() == 0):
    # print state of board
    print(g)

    # player X makes move (human)
    if g.turn == 1:
        move = input('X\'s move: ')

    # player O makes move (human)
    elif g.turn == -1:
        move = input('O\'s move: ')
    g.move(move)
    os.system('clear')


# print final game state and game result
print(g)
if(g.check() == 1):
    print('X wins!')
if(g.check() == -1):
    print('O Wins!')
if(g.check() == 2):
    print('Draw!')
