import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import sys

sys.path.insert(0, '../lib/')

from general_utils import plotSolution
from genetic_algorithm import geneticAlgorithm
from sudoku_utils import create_sudoku, remove_sudoku

initial_board = create_sudoku()
sudoku =  remove_sudoku(initial_board, porcentaje=0.3)
df = geneticAlgorithm(sudoku,totalSolutions=1000,iteraciones=10000,takeBest=100,tam=9,mutationRate=0.5)
print(df.iloc[-1]['sudoku'])
df.to_csv("../../results/results.csv")

plotSolution(sudoku)
plotSolution(df.iloc[-1]['sudoku'])