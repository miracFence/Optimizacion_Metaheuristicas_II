import pandas as pd
from matplotlib import pyplot as plt
import sys 

sys.path.insert(0, '../lib/')
from distUtils import getRandomCordinates
from genetic_algorithm import GeneticAlgorithm

isDistanceMatrix = True
dfResults = pd.DataFrame()

def readingData():
    global isDistanceMatrix
    if isDistanceMatrix:
        df = pd.read_csv("../../data/adjacency_matrix.csv", index_col=0)
    else:
        df = pd.DataFrame(getRandomCordinates(10), columns=['x', 'y'])
    
    return df

'''
def resultsAndPlotting():
    dfResults.to_csv('../../results/resultados.csv')
    if not isDistanceMatrix:
        plotAndSave(dfResults)'''

def main():
    global isDistanceMatrix
    df = readingData()
    dfResults = GeneticAlgorithm(df, matrixFormat = isDistanceMatrix, takeBest=10, maxiterations=10000)
    #resultsAndPlotting()
    dfResults.to_csv('../../results/resultados.csv')
    
if __name__ == "__main__":
    main()
