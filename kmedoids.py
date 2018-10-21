from scipy.spatial import distance
from random import randrange

def KMedoids(dataset, clusters):
	labels = [0] * len(dataset)
	centroids = [0] * clusters
	errors = float('inf')

	for i in range(0, len(centroids)):
		index = randrange(len(dataset))
		centroids[i] = dataset[index]

	assignCluster(dataset, centroids, labels)
	while(countErrors(dataset, centroids, labels) < errors):
		errors=countErrors(dataset, centroids, labels)
		randomChangeCentroid(dataset,centroids, labels)
		assignCluster(dataset, centroids, labels)

	return labels


def assignCluster(dataset, centroids, labels):
	for i in range(0, len(dataset)):
		dist = float('inf')
		for j in range(0, len(centroids)):
			manhattan = distance.cityblock(dataset[i],centroids[j])
			if (manhattan < dist):
				dist = manhattan
				labels[i] = j

def countErrors(dataset, centroids, labels):
	err = 0
	for i in range(0, len(dataset)):
		cluster = labels[i]
		err += distance.cityblock(dataset[cluster],centroids[cluster])
	return err

def randomChangeCentroid(dataset, centroids, labels):
	i = randrange(len(centroids))
	switch = randrange(len(dataset))
	if(labels[switch] != i):
		while(labels[switch] != i):
			switch = randrange(len(dataset))
	centroids[i] = dataset[switch]