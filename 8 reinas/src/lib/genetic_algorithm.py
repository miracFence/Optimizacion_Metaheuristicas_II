import pandas as pd
from nQueensUtils import fitness, clashes, crossOver, mutation

def GeneticAlgorithm(parents, takebest=8, iteraciones=100):
    res = []
    for i in range(iteraciones):        
        parents = fitness(parents)        
        res.append([parents[0],clashes(parents[0])])
        if(clashes(parents[0]) == 0):
            break
        parents = crossOver(parents,takebest)
        parents = mutation(parents)
    df = pd.DataFrame(res, columns=['solucion', 'conflictos'])
    return fitness(parents), df 