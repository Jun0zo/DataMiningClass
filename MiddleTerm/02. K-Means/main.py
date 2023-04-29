import math

ITERNUM = 5

data = [
    [1,3],
    [2,2],
    [2,3],
    [4,4],
    [4,5],
    [5,4],
]

def getL2(v1, v2):
    return math.sqrt(sum((x-y)**2 for x, y in zip(v1, v2)))

centroids = [[1,2], [4,3]]
clusters = [[] for _ in centroids]

for _ in range(ITERNUM):
    for vector_id, vector in enumerate(data):
        centroid_id = min(range(len(centroids)), key=lambda i: getL2(vector, centroids[i]))
        clusters[centroid_id].append(vector)
    
    print(centroids)
    for cluster_id, cluster in enumerate(clusters):
        new_centroid = [sum(x) / len(cluster) for x in zip(*cluster)]
        centroids[cluster_id] = new_centroid
    print(centroids)
    