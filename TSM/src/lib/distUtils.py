import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance_matrix

def getRandomCordinates(numbeOfCordinates, dimensions=2):
    return np.random.randint(0, numbeOfCordinates, (numbeOfCordinates, dimensions))


def getDistanceTwoNodes(df, point1, point2):
    if (point1 not in df.index or point2 not in df.index):
        return -1
    return df[point1][point2]


def getDistance(df, listOfPoints):
    totaldistance = 0
    # print(listOfPoints)
    for i in range(1, len(listOfPoints)):
        d = getDistanceTwoNodes(df, listOfPoints[i-1], listOfPoints[i])
        #print(d, listOfPoints[i-1], listOfPoints[i])
        if (d == -1):
            return -1
        totaldistance += d
    return totaldistance


def getDistanceMatrix(df):
    return pd.DataFrame(distance_matrix(df.values, df.values), columns=df.index, index=df.index)
