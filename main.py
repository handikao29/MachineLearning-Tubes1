from numpy import genfromtxt
import numpy as np
import pandas as pd
from dbscan import DBScan

def main():

    data_iris = genfromtxt('iris-data.csv', delimiter=',')
    data_iris_values = np.delete(data_iris, np.s_[4], 1)

    data_iris = genfromtxt('iris-data.csv', delimiter=',', dtype=int)
    data_iris_labels = np.delete(data_iris, np.s_[0:4], 1)
    data_iris_labels = np.concatenate(data_iris_labels)
    print(list(data_iris_labels))

    labels = DBScan(data_iris, 0.7, 15)
    print(labels)
    
    score = 0
    maxscore = 0
    for i in data_iris_labels:
        if (data_iris_labels[i] == labels[i]):
            score += 1
        maxscore += 1
    accuracy = score/maxscore
    print('Accuracy score: %.2f' % accuracy)
            
main()