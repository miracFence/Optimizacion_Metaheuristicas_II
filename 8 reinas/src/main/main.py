import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import sys

sys.path.insert(0, '../lib/')
from nQueensUtils import fitness, clashes, crossOver, mutation, plotSolution
from genetic_algorithm import GeneticAlgorithm

#NUMBER OF QUEENS
N = 8
res = [0] * N

def experiment(N):
    global res
   
    res, df = GeneticAlgorithm(N = N, takebest=N, iteraciones=10000)
    print(f"Positions of queens: {res[0]}; Number of clashes: {clashes(res[0])}")
    df.to_csv("../../results/resultados.csv")
    df.plot()
    
def main():
    global res 
    global N
    
    #Experiments
    experiment(N)
    
    #Plot Solutions
    plotSolution(res, N)
    
if __name__ == "__main__":
    main()