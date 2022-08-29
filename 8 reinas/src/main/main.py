import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import sys

sys.path.insert(0, '../lib/')
from nQueensUtils import fitness, clashes, crossOver, mutation
from genetic_algorithm import GeneticAlgorithm

#NUMBER OF QUEENS
N = 8
res = [0] * N

def experiment(N):
    global res
    positions = np.arange(N, dtype=int)
    positions = [np.random.permutation(positions) for i in range(N)] 

    res, df = GeneticAlgorithm(positions, takebest=N, iteraciones=10000)
    print(f"Positions of queens: {res[0]}; Number of clashes: {clashes(res[0])}")
    df.to_csv("../../results/resultados.csv")
    df.plot()

def plotSolution(solucion, n):
    fig = plt.figure(figsize=(n,n))
    ax = fig.add_subplot(111)
    ax.set_xlim(0,n)
    ax.set_ylim(0,n)

    for i in range(n):
        for j in range(n):
            if (i+j)%2==0:
                ax.add_patch(plt.Rectangle((i,j),1,1,facecolor='black'))
            else:
                ax.add_patch(plt.Rectangle((i,j),1,1,facecolor='white'))

    for i in range(n):
        ax.add_patch(plt.Circle((i+.5,solucion[0][i]+.5),0.4,facecolor='red'))

    plt.savefig("../../graphs/chessBoard.png")
    plt.show()
    
    
def main():
    global res 
    global N
    
    #Experiments
    experiment(N)
    
    #Plot Solutions
    plotSolution(res, N)
    
    
    
if __name__ == "__main__":
    main()