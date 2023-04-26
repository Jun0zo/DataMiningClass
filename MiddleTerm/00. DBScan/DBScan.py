import math
import matplotlib.pyplot as plt
import numpy as np
import random

def getL2(vector1, vector2):
    distance = 0
    x1, y1 = vector1
    x2, y2 = vector2
    distance += (x1-x2)**2 + (y1-y2)**2
    return math.sqrt(distance)

class DBSCAN:
    '''
        DBSCAN Class
        
        Attributes:
            data (list) : 데이터 리스트
            eps (float) : 클러스터를 위한 최소 이웃 거리
            min_pts (int) : 클러스터를 위한 최소 점의 개수
    '''
    def __init__(self, data: list =[], eps:float =2.5, min_pts:int =3):
        self.data = data
        self.labels = [-1] * len(data)
        self.eps = eps
        self.min_pts = min_pts
        self.cluster_id = 0
        
    def _get_neighbors(self, point: list) -> list:
        '''
         point과 이웃하는(eps거리보다 짧은) point를 list형태로 return하는 함수
            Args:
                input (list) : [x,y]형태로 주어짐
            Returns:
                output (list) : [[x1,y1], [x2,y2]...] 형태로 이웃하는 point들을 return
        '''
        return [point2_idx for point2_idx, point2 in enumerate(self.data) if getL2(point, point2) < self.eps]
    
    def _expand_cluster(self, neighbor_idxs) -> None:
        '''
        이웃하는 point들을 추가적으로 검사하는 함수
            Args:
                point (list) : [idx1, idx2 ...]형태로 주어짐
            Returns:
                output (None)
        '''
        # 모든 점들을 순회
        for neighbor_idx in neighbor_idxs:
            # 한번도 방문한 적이 없으면
            if self.labels[neighbor_idx] == -1:
                self.labels[neighbor_idx] = self.cluster_id
                new_neighbor_idxs = self._get_neighbors(self.data[neighbor_idx])
                # 한번도 방문한 적이 없고, CorePoint조건을 만족하면 클러스터에 추가
                if len(new_neighbor_idxs) > self.min_pts:
                    neighbor_idxs.extend(new_neighbor_idxs)
            elif self.labels[neighbor_idx] != self.cluster_id:
                self.labels[neighbor_idx] = 0
                break
   
    def clustering(self):
        '''
        DBSCAN방법으로 클러스터링하는 함수
        '''
        # 모든 점들을 순회
        for point_idx, point in enumerate(self.data):
            # 이미 방문한 점은 pass
            if self.labels[point_idx] != -1:
                continue
            # 이웃한 점들을 검색
            neighbor_idxs = self._get_neighbors(point)
            # CorePoint조건을 만족하지 못하면 보류
            if len(neighbor_idxs) < self.min_pts:
                self.labels[point_idx] = -1
                continue
            # CorePoint조건을 만족하면 클러스터에 추가
            self.cluster_id += 1
            self.labels[point_idx] = self.cluster_id
            # CorePoint의 이웃점들을 추가로 순회
            self._expand_cluster(neighbor_idxs)
        print(self.labels)
        
    def plotting(self):
       # create a list of colors for each label
        label_cnt = len(set(self.labels))
        color_pattelte = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in range(label_cnt+1)]
        print(color_pattelte)
        colors = [color_pattelte[label] for label in self.labels]

        plt.scatter([point[0] for point in self.data], [point[1] for point in self.data], c=colors)
        plt.title('DBSCAN Clustering')
        plt.show()