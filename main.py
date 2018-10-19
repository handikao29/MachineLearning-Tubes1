import numpy as np
from dbscan import DBScan

def main():
    
    iris = np.array([
        [1,3,4,5],
        [2,3,1,2],
        [4,5,3,4]
        ])
    print(iris)
    labels = DBScan(iris, 1, 1)
    print(labels)

main()