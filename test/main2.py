import random
import math
data = [
    [1,1],
    [2,1],
    [1,2],
    [5,5],
    [6,5],
    [5,6],
    [7,7],
]

def getL2(vector1, vector2):
    return math.sqrt(sum([(feature1 - feature2) **2 for feature1, feature2 in zip(vector1, vector2)]))

def clustering(data, K):
    for _ in range(10):
        # centroid = [[random.randrange(1,7), random.randrange(1,7)] for _ in range(K)]
        # centroid = [[1,1], [5,5]]
        clusters = [[] for _ in range(K)]
        for vector in data:
            min_idx = min(range(K), key=lambda idx: getL2(vector, centroid[idx]))
            clusters[min_idx].append(vector)
            
        print('===============')
        print(clusters)
        for cluster_idx, vectors in enumerate(clusters):
            new_position = [sum(features)/len(features) for features in zip(*vectors)]
            clusters[cluster_idx] = new_position
        print(clusters)
    
clustering(data, 2)