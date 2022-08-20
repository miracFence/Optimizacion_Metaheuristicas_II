import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance_matrix
from distUtils import getRandomCordinates, getDistanceTwoNodes, getDistance, getDistanceMatrix

def mutation(paths):
    for path in paths[1:]:
        for i in range(np.random.randint(0, len(path)/2)):
            index = np.random.randint(0, len(path), 2)
            path[index[0]], path[index[1]] = path[index[1]], path[index[0]]
    return paths


def sortparents(parents, dfMatrix):
    return sorted(parents, key=lambda x: getDistance(dfMatrix, np.append(x, x[0])))

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

def GeneticAlgorithm(df, matrixFormat=False, totalPaths=100, maxCrossOverSize=5, takeBest=5, maxiterations=2000):
    resultados = []
    dfMatrix = df
    if(not matrixFormat):
        dfMatrix = getDistanceMatrix(df)
    paths = [np.random.permutation(df.index) for i in range(totalPaths)]

    for i in range(maxiterations):
        paths = sortparents(paths, dfMatrix)
        resultados.append((i, paths[0], getDistance(
            dfMatrix, np.append(paths[0], paths[0][0]))))
        paths = crossOver(paths[:takeBest],
                          np.random.randint(0, maxCrossOverSize))
        paths = mutation(paths)

    dfResults = pd.DataFrame(resultados, columns=[
                             'iteracion', 'path', 'distancia'])
    return dfResults
