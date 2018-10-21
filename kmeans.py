from scipy.spatial import distance
from random import randrange
import statistics as s
import numpy as np

def KMeans(dataset, clusters):
	labels = [0] * len(dataset)
	centroids = [0] * clusters
	newCentroids = [0] * clusters

	for i in range(0, len(centroids)):
		index = randrange(len(dataset))
		centroids[i] = dataset[index]

	assignCluster(dataset, centroids, labels)
	setCentroids(dataset, newCentroids, labels)

	while (np.array_equal(np.array(newCentroids), np.array(centroids)) == False):
		centroids = newCentroids
		assignCluster(dataset, centroids, labels)
		setCentroids(dataset, newCentroids, labels)

	return labels


def assignCluster(dataset, centroids, labels):
	for i in range(0, len(dataset)):
		dist = float('inf')
		for j in range(0, len(centroids)):
			euclidean = distance.euclidean(dataset[i],centroids[j])
			if (euclidean < dist):
				dist = euclidean
				labels[i] = j

def setCentroids(dataset, centroids, labels):
	for i in range(0, len(centroids)):
		members = []
		for j in range(0, len(dataset)):
			if (labels[j] == i):
				members.append(dataset[j])
		centroids[i] = [float(sum(l))/len(l) for l in zip(*members)]

