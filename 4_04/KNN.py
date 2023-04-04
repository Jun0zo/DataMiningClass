import math 

class KNN:
    def __init__(self, db):
        self.db = db

    def _similarity(self, row1, row2):
        total = 0
        # print('row1', row1)
        # print('row2', row2)
        # print(list(zip(row1.items(), row2.items())))
        for a, b in zip(row1.items(), row2.items()):
            (col1_k, col1_v) = a
            (col2_k, col2_v) = b
            if col1_k == 'cluster' or col1_k == 'name':
                continue
            total += math.sqrt((col1_v - col2_v)**2)
        return total

    def clustering(self, dst_row):
        sims_list = []
            
        for row in self.db:
            sim = self._similarity(dst_row[0], row)
            sims_list.append({'similarity':sim, 'cluster':row['cluster']})
        sims_list = sorted(sims_list, key=lambda sim : sim['similarity'])

        # print(len(sims_list)//2)
        close_list = sims_list[:len(sims_list)//2]
        true_list = list(filter(lambda close_info : close_info['cluster'] == True, close_list))
        if len(true_list) > len(close_list)/2:
            return True
        else:
            return False

        