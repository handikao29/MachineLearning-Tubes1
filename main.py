from numpy import genfromtxt
import numpy as np
from dbscan import DBScan

def main():

    data_iris = genfromtxt('iris-data.csv', delimiter=',')
    data_iris_values = np.delete(data_iris, np.s_[4], 1)

    data_iris = genfromtxt('iris-data.csv', delimiter=',', dtype=int)
    data_iris_labels = np.delete(data_iris, np.s_[0:4], 1)
    data_iris_labels = np.concatenate(data_iris_labels)

    labels = DBScan(data_iris, 1, 15)
    print(labels)
    
    score = 0
    maxscore = 0
    for i in range(0, len(data_iris_labels)):
        if (data_iris_labels[i] == labels[i]):
            score += 1
        maxscore += 1
    accuracy = score/maxscore
    print('Accuracy score (DBScan): %.2f' % accuracy)
            
main()