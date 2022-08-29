import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def clashes(poblacion):
    conflictos = 0
    for i in range(poblacion.shape[0]):
        for j in range(poblacion.shape[0]):
            if i != j:
                if poblacion[i] == poblacion[j]:
                    conflictos += 1
                if abs(i - j) == abs(poblacion[i] - poblacion[j]):
                    conflictos += 1
    return conflictos

def fitness(parents):
    return sorted(parents, key=lambda x: clashes(x))
    
def randomCrossOver(paths):
    index = np.random.randint(0, len(paths[0]), 2)
    selection = paths[0][index[0]:index[1]]
    mask = np.isin(paths[1], np.setdiff1d(paths[1], selection))
    return np.append(paths[1][mask], selection)

def crossOver(paths, totalPaths=10):
    newPaths = [paths[0]]
    for i in range(1, totalPaths):
        index = np.random.randint(0, len(paths), 2)
        newPaths.append(randomCrossOver([paths[index[0]], paths[index[1]]]))
    return newPaths

def mutation(paths, mutationRate=0.1):
    for i in range(1, len(paths)):
        if np.random.random() < mutationRate:
            index = np.random.randint(0, len(paths[0]), 2)
            paths[i][index[0]], paths[i][index[1]] = paths[i][index[1]], paths[i][index[0]]
    return paths