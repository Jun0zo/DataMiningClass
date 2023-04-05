import math
import random

class KMeans:
    def __init__(self, vectors, K):
        self.vectors = vectors
        self.depths = len(vectors[0]) - 1
        self.K = K
        self.centroid_vectors = [tuple(random.randint(1, 5) for _ in range(self.depths)) for _ in range(K)]

    def _getLorm2(self, vector1, vector2):
        total = 0
        for value1, value2 in zip(vector1[1:], vector2):
            total += (value1 - value2) ** 2
        return math.sqrt(total)
    
    def clustering(self, iter_n=3):
        for i in range(iter_n):
            print(f'============ {i} ==============')
            print(self.centroid_vectors)
            clusters = [[] for idx in range(self.K)]
            for vector_idx, vector in enumerate(self.vectors):
                distance_list = [(self._getLorm2(vector, centroid_vector), centroid_vector_idx) for centroid_vector_idx, centroid_vector in enumerate(self.centroid_vectors)]
                min_value = min(distance_list, key=lambda distance: distance[0])
                min_idx = distance_list.index(min_value)
                distance, centroid_vector_idx = distance_list[min_idx]
                clusters[centroid_vector_idx].append(vector[1:])
            
            for cluster_idx, cluster in enumerate(clusters):
                next_position = [round(sum(x)/len(x),2) for x in zip(*cluster)]
                print(self.centroid_vectors[cluster_idx], '->', next_position)
                self.centroid_vectors[cluster_idx] = next_position