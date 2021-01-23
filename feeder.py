import time
from copy import deepcopy

import numpy as np
import tensorflow.keras.utils as U

import gameplay as gp

from random_play import nextMove


class ReversiFeeder(U.Sequence):
    "Generates data for reversi model"

    def __init__(
        self,
        player1=nextMove,
        player2=nextMove,
        size_batch=8,
        num_batch=64,
        tm_epsoide=128,
    ):
        "Initialization"
        self.player1: int = player1
        self.player2: int = player2
        self.size_batch: int = size_batch
        self.num_batch: int = num_batch
        self.tm_epsoide: int = tm_epsoide

    def __len__(self):
        "Denotes the number of batches per epoch"
        return self.num_batch

    def __getitem__(self, index):
        "Generate one batch of data"
        board = gp.newBoard()
        p1 = self.player1
        p2 = self.player2
        p1time = self.tm_epsoide
        p2time = self.tm_epsoide
        (currColor, nextColor) = (0, 1)

        count = 0

        while not gp.gameOver(board):
            count = count + 1
            print(count)
            tmpBoard = deepcopy(board)
            t1 = time.time()
            posMove = p1(tmpBoard, currColor, p1time)
            t2 = time.time()
            p1time = p1time - (t2 - t1)

            if gp.valid(board, currColor, posMove):
                gp.doMove(board, currColor, posMove)
            else:
                return np.array(board)

            (p1, p2) = (p2, p1)
            (p1time, p2time) = (p2time, p1time)
            (currColor, nextColor) = (nextColor, currColor)

        return np.array(board)


if __name__ == "__main__":
    try:
        dg = ReversiFeeder()
        print(dg.__getitem__(0))
        input("Enter to continue -> ...")
    except Exception as e:
        print(e)
