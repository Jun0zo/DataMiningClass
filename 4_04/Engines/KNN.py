import math 
from .Types.DB import DB

class KNN:
    def __init__(self, vectors : tuple, K):
        self.vectors = vectors
        self.K = K
        
    def _getLorm2(self, vector1, vector2):
        total = 0
        for val1, val2 in zip(vector1[1:-1], vector2[1:-1]):
            total += (val1 - val2) ** 2
        return math.sqrt(total)

    def clustering(self, dst_vector):
        distance_list = []
        for vector in self.vectors:
            distance = self._getLorm2(dst_vector, vector)
            distance_list.append({'distance':distance, 'vector':vector})
        distance_list.sort(key=lambda distance_info : distance_info['distance'])
        print('거리가 가까운 순 : ')
        for distance in distance_list:
            print(distance)
        
        cluster_kind_list = [distance['vector'][-1] for distance in distance_list[:self.K]]
        print('제일 가까운 K개의 클러스터 : ', cluster_kind_list)
        
        max_cnt = 0
        max_kind = ''
        for kind in set(cluster_kind_list):
            cnt = cluster_kind_list.count(kind)
            if cnt > max_cnt:
                max_cnt = cnt
                max_kind = kind
                
        return max_kind
        
            
            