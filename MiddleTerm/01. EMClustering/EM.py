import random
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def normal_pdf(x, mean, standard_deviation):
        # x값, 평균, 표준편차로 probability density function (확률밀도함수)를 구하는 함수
        return (1 / (standard_deviation * math.sqrt(2 * math.pi))) * math.exp(-(x - mean)**2 / (2 * standard_deviation**2))

def normal_pdfs(x, mean, standard_deviation):
    # x값, 평균, 표준편차로 probability density function (확률밀도함수)를 구하는 함수
    normal_distribution = norm(loc=mean, scale=standard_deviation)
    return normal_distribution.pdf(x)

class EM:
    def __init__(self, data, K=2):
        self.data = data
        self.K = K
        
        # 각 정규분포의 확률, 평균, 표준편차를 저장하는 변수
        self.distributions = [{'weight':1/K, 'means':random.uniform(2,30), 'standard_deviation':random.uniform(1,10)} for _ in range(K)]
        # likelihood값을 저장하는 변수
        self.likelihoods = [[-1] * len(data) for _ in range(K)]
        self.clusters = [[] for _ in range(self.K)]
        

    def _EStep(self):
        # 각 distribution(가우시안분포)에 해당하는 x의 likelihood를 계산하여 저장
        for i, distribution in enumerate(self.distributions):
            for j, x in enumerate(self.data):
                weight, means, standard_deviation = distribution['weight'], distribution['means'], distribution['standard_deviation']
                likelihood = weight * normal_pdf(x, means, standard_deviation)
                self.likelihoods[i][j] = likelihood
        totals = sum(sum(row) for row in self.likelihoods) 
        
        # Normalization (정규화) - 전체 likelihood를 나눔
        for i, distribution in enumerate(self.distributions):
            for j, x in enumerate(self.data):
                self.likelihoods[i][j] /= totals
                

        # for i, x in enumerate(self.data):
        #     cluster_id = -1
        #     max_likelihood = -1
        #     for j, distribution in enumerate(self.distributions):
        #         likelihood = self.likelihoods[j][i]
        #         if max_likelihood < likelihood:
        #             cluster_id = j
        #             max_likelihood = likelihood
        #     self.clusters[cluster_id].append(x)
                
        
    def _MStep(self):
        # 각 distribution(가우시안분포)의 확률, 평균, 분산을 업데이트
        for i, distribution in enumerate(self.distributions):
            # 각 distribution(가우시안분포)의 확률을 업데이트
            weight_sum = sum(self.likelihoods[i])
            self.distributions[i]['weight'] = weight_sum / len(self.likelihoods[i])
            
            # 각 distribution(가우시안분포)의 평균을 업데이트
            mean_num = sum([self.likelihoods[i][j] * self.data[j] for j in range(len(self.data))])
            mean_denom = sum(self.likelihoods[i])
            self.distributions[i]['means'] = mean_num / mean_denom
            
            # 각 distribution(가우시안분포)의 분산을 업데이트
            std_num = sum([self.likelihoods[i][j] * ((self.data[j] - distribution['means']) ** 2) for j in range(len(self.data))])
            std_denom = sum(self.likelihoods[i])
            self.distributions[i]['standard_deviation'] = math.sqrt(std_num / std_denom)
        
        weight_sum_total = sum([distribution['weight'] for distribution in self.distributions])
        for distribution in self.distributions:
            distribution['weight'] /= weight_sum_total

    def clustering(self):
        # E-step과 M-step 반복
        for _ in range(100):
            self.clusters = [[] for _ in range(self.K)]
            self._EStep()
            self._MStep()
            
        self.print_cluster()
        
        
    def print_cluster(self):
        print('클러스터 목록')
        for i, cluster in enumerate(self.clusters):
            print(f'{i} : {cluster}')