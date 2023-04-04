import math
import random

class KMeans:
    def __init__(self, db, K):
        self.db = db
        self.K = K

    def _similarity(self, row1, row2):
        total = 0
        
        for a, b in zip(row1.items(), row2):
            (col1_k, col1_v) = a
            if col1_k == 'cluster' or col1_k == 'name':
                continue
            total += math.sqrt((col1_v - b)**2)
        return total

    def clustering(self, iter_n=10):
        rows = self.db
        depths = len(rows[0]) - 1
        
        centroid_list = [ [random.randint(1,5) for _ in range(depths)] for _ in range(self.K)]
        print('initial :', centroid_list)

        for idx in range(iter_n):
            print(f'==============={idx}===================')
            update_dict = {} # {'1': [1,2,3], '2': [4,5,6]}
            for row_idx, row in enumerate(rows):
                if row.get('name'):
                    row.pop('name')
                sim_list = []
                for centroid in centroid_list:
                    sim = self._similarity(row, centroid)
                    sim_list.append(sim)
                min_value = min(sim_list)
                closest_centroid_idx = sim_list.index(min_value)
                if not update_dict.get(closest_centroid_idx):
                    update_dict[closest_centroid_idx] = []
                update_dict[closest_centroid_idx].append(row_idx)


            for update_key, dst_row_idxs in update_dict.items():

                update_position = []
                total_list = [0] * depths
                for dst_row_idx in dst_row_idxs:  # 점 하나
                    dst_row = rows[dst_row_idx]
                    
                    for col_idx, col in enumerate(dst_row.items()):
                        col_name, col_val = col
                        if col_name == 'name':
                            continue
                        total_list[col_idx] += col_val
                for total in total_list:
                    means = total // depths
                    update_position.append(means)
                    
                print()
                print(centroid_list[update_key], '->', update_position)
                centroid_list[update_key] = update_position

                print('result :', centroid_list)
        
        
        