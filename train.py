import numpy as np
import random
import pickle
import brain
import game
import os
import copy
import time

# Play a game using 2 brains and update thier scores
def play(A, B):

    # create new game
    g = game.Game()

    # play game
    while(g.check() == 0):

        # print state of board
        #os.system('clear')
        #print('brains: {0}[score={2}](X) vs {1}[score={3}](O)'.format(A.ID,B.ID,A.score,B.score))
        #print(g)

        # player X makes move (brain)
        if g.turn == 1:
            move = A.suggest(g.state)
            #time.sleep(0.1)
            g.move(move)

        # player O makes move (brain)
        elif g.turn == -1:
            move = B.suggest(g.state)
            #time.sleep(0.1)
            g.move(move)

        # print final game state and game result
        #os.system('clear')
        #print(g)
        if(g.check() == 1):
            #print('X wins!')
            A.score += 1
            B.score -= 1
        if(g.check() == -1):
            #print('O Wins!')
            A.score -= 1
            B.score += 1
        if(g.check() == 2):
            print('Draw!')

def breed(A, B, ID, N=200, M=5.0):

    # create breeding patterns
    W1P = np.random.randint(0, 2, A.W1.shape)
    W2P = np.random.randint(0, 2, A.W2.shape)
    W3P = np.random.randint(0, 2, A.W3.shape)
    B1P = np.random.randint(0, 2, A.B1.shape)
    B2P = np.random.randint(0, 2, A.B2.shape)
    B3P = np.random.randint(0, 2, A.B3.shape)
    
    # breed A.B -> C
    C = brain.Brain(ID=ID)
    C.W1[:,:] = A.W1[:,:]*W1P[:,:] + B.W1[:,:]*(1-W1P[:,:])
    C.W2[:,:] = A.W2[:,:]*W2P[:,:] + B.W2[:,:]*(1-W2P[:,:])
    C.W3[:,:] = A.W3[:,:]*W3P[:,:] + B.W3[:,:]*(1-W3P[:,:])
    C.B1[:] = A.B1[:]*B1P[:] + B.B1[:]*(1-B1P[:])
    C.B2[:] = A.B2[:]*B2P[:] + B.B2[:]*(1-B2P[:])
    C.B3[:] = A.B3[:]*B3P[:] + B.B3[:]*(1-B3P[:])

    # mutate C
    Nr = random.randint(0,N)
    for _ in range(Nr):
        C.W1[np.random.randint(0,C.W1.shape[0]),np.random.randint(0,C.W1.shape[1])] += (random.random()*2*M)-M
        C.W2[np.random.randint(0,C.W2.shape[0]),np.random.randint(0,C.W2.shape[1])] += (random.random()*2*M)-M
    for _ in range(int(Nr/2)):
        C.W3[np.random.randint(0,C.W3.shape[0]),np.random.randint(0,C.W3.shape[1])] += (random.random()*2*M)-M
    for _ in range(random.randint(0,int(Nr/16))):
        C.B1[np.random.randint(0,C.B1.shape[0])] += (random.random()*2*M)-M
        C.B2[np.random.randint(0,C.B2.shape[0])] += (random.random()*2*M)-M
        C.B3[np.random.randint(0,C.B3.shape[0])] += (random.random()*2*M)-M

    return C

def main():

    N = 10 # temp
    # create initial population
    gID = 0
    brains = []
    for i in range(0, N):
        brains.append(brain.Brain(ID=i))
        gID += 1

    it = 0
    while True:

        # play one round of games
        for i in range(0, N):
            for j in range(0, N):
                if i != j:
                    play(brains[i], brains[j])
        #os.system('clear')

        # print scores
        for i in range(0, N):
            print('inter={2}: ID={0}, score={1}'.format(brains[i].ID, brains[i].score,it))

        # select best 4 brains
        scores = np.zeros((N,2))
        for i in range(0,N):
            scores[i,1] = brains[i].score
            scores[i,0] = brains[i].ID
        scores = scores[scores[:,1].argsort()]
        best_brains_id = scores[N-4:N,0]
        best_brains = []
        for b in brains:
            if any(best_brains_id == b.ID):
                best_brains.append(b)
        #for b in best_brains:
            #print(b.ID)

        # breed best brains
        new_brains = []
        for b in best_brains:
            new_brains.append(b)
        for i in range(0,4):
            for j in range(0,i+1):
                if i != j:
                    new_brain = breed(best_brains[i], best_brains[j], ID = gID)
                    gID += 1
                    new_brains.append(new_brain)
        brains = copy.deepcopy(new_brains)
        for b in brains:
            b.score = 0
        if it % 100 == 0:
            print('saving brain to brain{0}_{1}.db'.format(brains[0].ID,it))
            pickle.dump(brains[0], open('brain{0}_{1}.db'.format(brains[0].ID,it), 'wb'))
            
        it += 1 
    

if __name__ == '__main__':
    main()
