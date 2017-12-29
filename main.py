# Main run file
import os
import time
import numpy as np
import game
import brain

# create new game
g = game.Game()

# load in opponent
b = brain.Brain()

# main game loop
while(g.check() == 0):

    # print state of board
    os.system('clear')
    print(g)

    # player X makes move (human)
    if g.turn == 1:
        move = input('X\'s move: ')

    # player O makes move (brain)
    elif g.turn == -1:
        move = b.suggest(g.state)
        time.sleep(2)
    g.move(move)

# print final game state and game result
os.system('clear')
print(g)
if(g.check() == 1):
    print('X wins!')
if(g.check() == -1):
    print('O Wins!')
if(g.check() == 2):
    print('Draw!')
