import math
import random

class KMeans:
    def __init__(self, vectors, K):
        self.vectors = vectors
        self.depths = len(vectors[0]) - 1
        self.K = K
        # 센트로이드 리스트를 벡터형태로 가지고 있음
        self.centroid_vectors = [tuple(random.randint(1, 5) for _ in range(self.depths)) for _ in range(K)]

    # 유클리드 거리를 구하는 함수
    def _getLorm2(self, vector1, vector2):
        total = 0
        for value1, value2 in zip(vector1[1:], vector2):
            total += (value1 - value2) ** 2
        return math.sqrt(total)
    
    # Kmeans
    def clustering(self, iter_n=3):
        # 이터레이션 수 만큼 반복
        for i in range(iter_n):
            print(f'{i+1}번째 이터레이션에서의 센트로이드 값 : ', self.centroid_vectors)
            clusters = [[] for idx in range(self.K)]
            
            # 모든 벡터에 대해 각 센트로이드와의 거리를 구한다
            for vector_idx, vector in enumerate(self.vectors):
                distance_list = [(self._getLorm2(vector, centroid_vector), centroid_vector_idx) for centroid_vector_idx, centroid_vector in enumerate(self.centroid_vectors)]
                min_value = min(distance_list, key=lambda distance: distance[0])
                min_idx = distance_list.index(min_value)
                distance, centroid_vector_idx = distance_list[min_idx]
                # 거리가 가장 가까운 센트로이드의 클러스터에 추가
                clusters[centroid_vector_idx].append(vector[1:])
            
            # 최종적으로 추가된 센트로이드의 클러스터에 존재하는 벡터들을 기반으로 센트로이드의 다음 벡터를 계산
            for cluster_idx, cluster in enumerate(clusters):
                next_position = [round(sum(x)/len(x),2) for x in zip(*cluster)]
                # 새롭게 계산된 센트로이드의 좌표를 업데이트한다.
                self.centroid_vectors[cluster_idx] = next_position