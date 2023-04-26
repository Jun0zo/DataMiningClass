import random
import math
import matplotlib.pyplot as plt
import numpy as np

def normal_pdf(x, mean, standard_deviation):
        # x값, 평균, 표준편차로 probability density function (확률밀도함수)를 구하는 함수
        return (1 / (standard_deviation * math.sqrt(2 * math.pi))) * math.exp(-(x - mean)**2 / (2 * standard_deviation**2))
class EM:
    def __init__(self, data, K):
        self.data = data
        self.K = K
        
        # 각 정규분포의 확률, 평균, 표준편차를 저장하는 변수
        self.distributions = [{'weight':1/K, 'means':random.uniform(-1,5), 'standard_deviation':1} for _ in range(K)]
        # likelihood값을 저장하는 변수
        self.likelihoods = [[-1] * len(data) for _ in range(K)]

    def _EStep(self):
        totals = 0
        # 각 distribution(가우시안분포)에 해당하는 x의 likelihood를 계산하여 저장
        for i, distribution in enumerate(self.distributions):
            for j, x in enumerate(self.data):
                weight, means, standard_deviation = distribution['weight'], distribution['means'], distribution['standard_deviation']
                likelihood = weight * normal_pdf(x[0], means, standard_deviation)
                self.likelihoods[i][j] = likelihood
                totals += likelihood
        
        # Normalization (정규화) - 전체 likelihood를 나눔
        for i, distribution in enumerate(self.distributions):
            for j, x in enumerate(self.data):
                self.likelihoods[i][j] = likelihood / totals
        
    def _MStep(self):
        # 각 distribution(가우시안분포)의 확률, 평균, 분산을 업데이트
        for i, distribution in enumerate(self.distributions):
            # 각 distribution(가우시안분포)의 확률을 업데이트
            weight_sum = sum(self.likelihoods[i])
            self.distributions[i]['weight'] = weight_sum / len(self.data)
            
            # 각 distribution(가우시안분포)의 평균을 업데이트
            mean_num = sum([self.likelihoods[i][j] * self.data[j][0] for j in range(len(self.data))])
            mean_denom = weight_sum
            self.distributions[i]['means'] = mean_num / mean_denom
            
            # 각 distribution(가우시안분포)의 분산을 업데이트
            std_num = sum([self.likelihoods[i][j] * ((self.data[j][0] - distribution['means']) ** 2) for j in range(len(self.data))])
            std_denom = weight_sum
            self.distributions[i]['standard_deviation'] = math.sqrt(std_num / std_denom)

    def clustering(self):
        for _ in range(100):
            self._EStep()
            self._MStep()

    def plotting(self):
        x = np.linspace(-10, 10, 500)
        y = np.zeros((self.K, len(x)))

        for i, distribution in enumerate(self.distributions):
            weight, mean, std = distribution['weight'], distribution['means'], distribution['standard_deviation']
            for j in range(len(x)):
                y[i][j] = weight * normal_pdf(x[j], mean, std)

            plt.plot(x, y[i], label="Gaussian {}".format(i))

        plt.hist(self.data, density=True, alpha=0.5)
        plt.legend()
        plt.show()
