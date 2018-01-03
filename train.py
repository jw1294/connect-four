import numpy as np
import brain
import game
import os
import time

# Play a game using 2 brains and update thier scores
def play(A, B):

    # create new game
    g = game.Game()

    # play game
    while(g.check() == 0):

        # print state of board
        os.system('clear')
        print('brains: {0}[score={2}](X) vs {1}[score={3}](O)'.format(A.ID,B.ID,A.score,B.score))
        print(g)

        # player X makes move (brain)
        if g.turn == 1:
            move = A.suggest(g.state)
            time.sleep(0.1)
            g.move(move)

        # player O makes move (brain)
        elif g.turn == -1:
            move = B.suggest(g.state)
            time.sleep(0.1)
            g.move(move)

        # print final game state and game result
        os.system('clear')
        print(g)
        if(g.check() == 1):
            print('X wins!')
            A.score += 1
            B.score -= 1
        if(g.check() == -1):
            print('O Wins!')
            A.score -= 1
            B.score += 1
        if(g.check() == 2):
            print('Draw!')

def main():

    # create initial population
    brains = []
    for i in range(0, 10):
        brains.append(brain.Brain(ID=i))

    # play one round of games
    for i in range(0, 10):
        for j in range(0, 10):
            if i != j:
                play(brains[i], brains[j])
    os.system('clear')

    # print scores
    for i in range(0, 10):
        print('ID={0}, score={1}'.format(brains[i].ID, brains[i].score))

if __name__ == '__main__':
    main()
