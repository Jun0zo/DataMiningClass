import copy
import math

data = [
    (1,1),
    (1,2),
    (2,1),
    (5,5),
    (5,6),
    (6,5),
    (7,7),
]

clusters = [[vector] for vector in data]

def getL2(v1, v2):
    return math.sqrt(sum([(x-y)**2 for x, y in zip(v1,v2)]))

def getClusterL2(cluster1, cluster2):
    return min([getL2(vector1, vector2) for vector1 in cluster1 for vector2 in cluster2])

def mergeCluster(cluster_idx1, cluster_idx2):
    clusters[cluster_idx1].extend(clusters[cluster_idx2])
    del clusters[cluster_idx2]

def printClusters():
    for c in clusters:
        print(c)
    print("==============")

while len(clusters) > 1:
    printClusters()
    distances, (vector_idx1, vector_idx2) = sorted([(getClusterL2(clusters[idx1], clusters[idx2]), (idx1, idx2)) for idx1, _ in enumerate(clusters) for idx2, _ in enumerate(clusters) if idx2 > idx1])[0]
    mergeCluster(vector_idx1, vector_idx2)
printClusters()