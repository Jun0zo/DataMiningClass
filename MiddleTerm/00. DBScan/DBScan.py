import math
import matplotlib.pyplot as plt
import numpy as np
import random

class DBScan:
    def __init__(self, data=[]):
        self.data = data
        self.labels = [-1] * len(data)
        self.eps = 2.5
        self.min_pts = 3
        
        self.cluster_id = 0
        
    def getL2(self, i, vector1, vector2):
        distance = 0
        x1, y1 = vector1
        x2, y2 = vector2
        distance += (x1-x2)**2 + (y1-y2)**2
        return math.sqrt(distance)
        
    def get_neighbors(self, point1):
        return [point2_idx for point2_idx, point2 in enumerate(self.data) if self.getL2(point2_idx, point1, point2) < self.eps]

    def is_center(self, point1):
        return True if len(self.get_neighbors(point1)) > self.min_pts else False
    
    def expand_cluster(self, idx, neighbor_idxs):
        for neighbor_idx in neighbor_idxs:
            if self.labels[neighbor_idx] == -1:
                self.labels[neighbor_idx] = self.cluster_id
                new_neighbor_idxs = self.get_neighbors(self.data[neighbor_idx])
                if len(new_neighbor_idxs) > self.min_pts:
                    neighbor_idxs.extend(new_neighbor_idxs)
            elif self.labels[neighbor_idx] != self.cluster_id:
                self.labels[neighbor_idx] = 0
                break
   
    def clustering(self):
        for point_idx, point in enumerate(self.data):
            if self.labels[point_idx] != -1:
                continue
            neighbor_idxs = self.get_neighbors(point)
            if len(neighbor_idxs) < self.min_pts:
                self.labels[point_idx] = -1
                continue
            self.cluster_id += 1
            self.labels[point_idx] = self.cluster_id
            self.expand_cluster(point_idx, neighbor_idxs)
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