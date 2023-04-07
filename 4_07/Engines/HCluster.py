import math 
import copy
from .Types.DB import DB

# 계층적 클러스터
class HCluster:
    def __init__(self, vectors : tuple):
        self.vectors = vectors
        self.clusters = [[vector] for vector in vectors]
        self.history = {}
        
    # 유클리드 거리를 구하는 함수
    def _getLorm2(self, vector1, vector2):
        total = 0
        for val1, val2 in zip(vector1, vector2):
            total += (val1 - val2) ** 2
        return math.sqrt(total)

    # 클러스터끼리의 거리를 계산
    def getClusterDistance(self, cluster1, cluster2, method):
        max_distance = -1
        for vector1 in cluster1:
            for vector2 in cluster2:
                max_distance = max(max_distance, self._getLorm2(vector1[1:], vector2[1:]))
        return max_distance
    
    # 클러스터끼리 합치는 함수
    def link(self, link1_idx, link2_idx, method):
        cluster2 = self.clusters[link2_idx]
        self.clusters[link1_idx].extend(cluster2)
        self.clusters.pop(link2_idx)

    # 계층적 군집분석
    def clustering(self, dst_vector, cutoff):
        n = len(self.clusters)
        
        # 클러스터의 개수가 1개 될때까지 계속 반복
        while len(self.clusters) > 1:
            self.history[n] = copy.deepcopy(self.clusters)
            if n == cutoff:
                print(f'{n}개의 클러스터로 구성')
                for cluster in self.clusters:
                    print(cluster)
            # 최솟값을 찾는 과정
            min_distance = 1e9

            link1_idx, link2_idx = -1, -1
            # 모든 클러스터들의 경우의 수를 구함
            for cluster1_idx, cluster1 in enumerate(self.clusters):
                for cluster2_idx, cluster2 in enumerate(self.clusters):
                    # 서로 다른 클러스터일 때
                    if cluster1 != cluster2:
                        # 가장 가까운 클러스터를 찾는다 
                        distance = self.getClusterDistance(cluster1, cluster2, method='min')
                        if distance < min_distance:
                            min_distance = distance
                            link1_idx, link2_idx = cluster1_idx, cluster2_idx
            # 2개의 클러스터를 합침
            self.link(link1_idx, link2_idx, method='min')  
            n -= 1
            
            