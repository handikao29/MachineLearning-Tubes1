from scipy.spatial import distance

# def distance(p,q):
#     return math.sqrt()


def DBScan(dataset, epsilon, minPts):
    labels = [0]*len(dataset)
    cluster_id = 0
    for x in range(0, len(dataset)):
        if (labels[x] == 0):
            neighborPts = regionOfPoint(dataset, x, epsilon)

            if (len(neighborPts) < minPts):
                labels[x] = -1
            else:
                cluster_id += 1
                assignCluster(dataset, labels, x, neighborPts, cluster_id, epsilon, minPts)

    return labels

def regionOfPoint(dataset, x, epsilon):
    neighbors = []
    for point in range (0, len(dataset)):
        # if (numpy.linalg.norm(dataset[x] - dataset[point]) < epsilon):
        if (distance.euclidean(dataset[x], dataset[point]) < epsilon):
           neighbors.append(point)
    return neighbors

def assignCluster(dataset, labels, x, neighborPts, cluster_id, epsilon, minPts):
    labels[x] = cluster_id
    i = 0
    while i < len(neighborPts):
        point = neighborPts[i]
        if labels[point] == 0:
            labels[point] = cluster_id
            pointOfNeighborPts = regionOfPoint(dataset,point,epsilon)
            
            if (len(pointOfNeighborPts) >= minPts):
                neighborPts = neighborPts + pointOfNeighborPts
            
        elif labels[point] == -1:
            labels[point] = cluster_id

        i += 1