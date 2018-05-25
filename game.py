# This file will handle all of the Connect Four game logic
import numpy as np

# Class to contain all game info and possible actions
# Game
# ----
# state[7,7]   0 -> Empty
#              1 -> X
#             -1 -> O
#
# turn         1 -> X
#             -1 -> O
#
# move(y)      True -> Legal and changed
#              False -> Illegal and unchanged
#
# check()      0 -> None
#              1 -> X
#             -1 -> O
#              2 -> Draw
#
# print(g)     prints

class Game:

    def __init__(self):
        self.state = np.zeros(shape=(7,7),dtype=np.int)
        self.turn = int(1)

    def move(self, y):
        try:
            y = int(y)
        except:
            return False
        if y not in [0,1,2,3,4,5,6]:
            return False
        col = self.state[:,y]
        if 0 in col:
            x = np.max(np.where(col==0))
            self.state[x,y] = int(self.turn)
            self.turn *= -1
            return True
        else:
            return False

    def check(self):
        for i in range(0, 7):
            row = self.state[i,:]
            if contain(row.tolist(), [1,1,1,1]):
                return 1
            elif contain(row.tolist(), [-1,-1,-1,-1]):
                return -1
        for j in range(0, 7):
            col = self.state[:,j]
            if contain(col.tolist(), [1,1,1,1]):
                return 1
            elif contain(col.tolist(), [-1,-1,-1,-1]):
                return -1
        for k in range(-3, 4):
            diag = np.diag(self.state, k=k)
            if contain(diag.tolist(), [1,1,1,1]):
                return 1
            elif contain(diag.tolist(), [-1,-1,-1,-1]):
                return -1
        for l in range(-3, 4):
            diag = np.diag(np.fliplr(self.state), k=l)
            if contain(diag.tolist(), [1,1,1,1]):
                return 1
            elif contain(diag.tolist(), [-1,-1,-1,-1]):
                return -1
        if 0 not in self.state:
            return 2
        return 0

    def __str__(self):
        s = ''
        for i in range(0, 7):
            for j in range(0, 7):
                if self.state[i,j] == 0:
                    s += '-'
                elif self.state[i,j] == 1:
                    s += 'X'
                elif self.state[i,j] == -1:
                    s += 'O'
                else:
                    raise ValueError('non-valid value in state')
            s += '\n'
        if self.turn == 0:
            s += 'turn: GAME OVER'
        elif self.turn == 1:
            s += 'turn: X'
        elif self.turn == -1:
            s += 'turn: O'
        else:
            raise ValueError('non-valid value in state')
        return s


def contain(A, B):
    n=-1
    while True:
        try:
            n = A.index(B[0],n+1)
        except ValueError:
            return False
        if A[n:n+len(B)]==B:
            return True
