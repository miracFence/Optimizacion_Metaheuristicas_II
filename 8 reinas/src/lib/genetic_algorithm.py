import pandas as pd
import numpy as np
from nQueensUtils import fitness, clashes, crossOver, mutation

def GeneticAlgorithm(N = 8, takebest=8, iteraciones=100):
    
    #initial population
    parents = np.arange(N, dtype=int)
    parents = [np.random.permutation(parents) for i in range(N)] 

    res = []
    for i in range(iteraciones):        
        parents = fitness(parents)        
        res.append([parents[0],clashes(parents[0])])
        if(clashes(parents[0]) == 0):
            print(f"Iteración de convergencia inicial: {i}")
            break
        parents = crossOver(parents,takebest)
        parents = mutation(parents)
    df = pd.DataFrame(res, columns=['solucion', 'conflictos'])
    return fitness(parents), df 