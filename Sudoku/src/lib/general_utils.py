import numpy as np 
import matplotlib.pyplot as plt
import sys

sys.path.insert(0, '../lib/')

def plotSolution(sudoku,n = 9):        
    fig, ax = plt.subplots(figsize=(n, n))   
    ax.set_title('Sudoku') 
    ax.set_xlim(0,n)
    ax.set_ylim(0,n)
    major_ticks = np.arange(0, n, n/3)
    minor_ticks = np.arange(0, n, 1)
    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(major_ticks)
    ax.set_yticks(minor_ticks, minor=True)
    ax.grid(which='both')
    ax.grid(which='minor', alpha=0.3)
    ax.grid(which='major', alpha=0.9,linewidth=2)
    for i in range(n):
        for j in range(n):
            text = ax.text(j+.5, i+.5, sudoku[i, j], ha="center", va="center", color="r")
    plt.savefig("../../graphs/sudoku_final_result.png")
    plt.title("Sudoku results")
    plt.show()