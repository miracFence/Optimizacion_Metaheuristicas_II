import numpy as np 
import random

def create_sudoku():
    base  = 3
    side  = base*base

    # pattern for a baseline valid solution
    def pattern(r,c): 
        return (base*(r%base)+r//base+c)%side

    # randomize rows, columns and numbers (of valid base pattern)
    def shuffle(s): 
        return random.sample(s,len(s)) 
    
    rBase = range(base) 
    rows  = [g*base + r for g in shuffle(rBase) for r in shuffle(rBase)] 
    cols  = [g*base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums  = shuffle(range(1,base*base+1))

    # produce board using randomized baseline pattern
    board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

    return np.array(board)

def remove_sudoku(sudoku, porcentaje=.5):
    # remove numbers from sudoku
    sudoku = sudoku.copy()
    for i in range(9):
        for j in range(9):
            if np.random.rand() < porcentaje:
                sudoku[i,j] = 0
    return sudoku.astype(np.int64)