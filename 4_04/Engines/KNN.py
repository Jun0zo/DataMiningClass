import math 
from .Types.DB import DB

class KNN:
    def __init__(self, vectors : tuple, K):
        self.vectors = vectors
        self.K = K
        
    # 유클리드 거리를 구하는 함수
    def _getLorm2(self, vector1, vector2):
        total = 0
        for val1, val2 in zip(vector1[1:-1], vector2[1:-1]):
            total += (val1 - val2) ** 2
        return math.sqrt(total)

    # KNN
    def clustering(self, dst_vector):
        distance_list = []
        # 모든 점에 대해 각 점으로의 거리를 구하고 정렬한다.
        for vector in self.vectors:
            distance = self._getLorm2(dst_vector, vector)
            distance_list.append({'distance':distance, 'vector':vector})
        distance_list.sort(key=lambda distance_info : distance_info['distance'])
        print('거리가 가까운 순 : ')
        for distance in distance_list:
            print(distance)
        
        # 정렬된 리스트를 K개로 자른다. (가장 가까운 벡터 K개를 구하는 단계)
        cluster_kind_list = [distance['vector'][-1] for distance in distance_list[:self.K]]
        print('제일 가까운 K개의 클러스터 : ', cluster_kind_list)
        
        max_cnt = 0
        max_kind = ''
        # 가까운 거리에 위치한 K개의 벡터의 클러스터 중 최빈값에 해당되는 클러스터를 구한다.
        for kind in set(cluster_kind_list):
            cnt = cluster_kind_list.count(kind)
            if cnt > max_cnt:
                max_cnt = cnt
                max_kind = kind
                
        return max_kind
        
            
            