import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from Loss import CE
plt.rcParams['agg.path.chunksize'] = 10000


class LinearClassification:
    def __init__(self, x_data, y_data, loss='l1'):
        # x, y, W, b를 초기화
        self.x_data = x_data
        self.y_data = y_data
        self.W_list = np.array([2.,1.5]) # np.random.rand(x_data.shape[1])
        self.b = np.random.rand(1)
        self.N = x_data.shape[0]
        
        # loss를 담는 list
        self.loss_hist = []
        
        # learning rate설정
        self.lr = 0.00008
        
        # 손실함수 정의
        self.lossF = CE()
        
        os.makedirs('./result/linear_classification/3d', exist_ok=True)
        os.makedirs('./result/linear_classification/2d', exist_ok=True)

    def gradient_desent(self):
        # y에 대한 예측값 계산
        y_hat = np.sum(self.W_list * self.x_data, axis=1) + self.b
        
        # 손실값 계산
        loss = self.lossF(y_hat, self.y_data)
        self.loss_hist.append(loss)
        
        # w와 b업데이트 값 계산
        w_grads = np.sum(self.x_data * np.reshape(y_hat - self.y_data, (-1,1)) / self.N, axis=0)
        b_grad = np.sum((y_hat - self.y_data) / self.N, axis=0)
        
        # 경사 하강법으로 파라미터 업데이트
        self.W_list -= self.lr * w_grads
        self.b -= self.lr * b_grad
        
        return loss
        
    def foward(self, x=None):
        if x is not None:
            return np.sum(self.W_list.reshape(1, -1) * x.reshape(-1,1), axis=1) + self.b
        else:
            return np.sum(self.W_list * self.x_data, axis=1) + self.b
        
    def foward_filter(self):
        return self.W_list.reshape(1, -1) * self.x_data + self.b
        
    def plotting_loss(self):
        fig = plt.figure(figsize = (10,7))
        ax = fig.add_subplot(111)
        ax.plot(range(len(self.loss_hist)), self.loss_hist)
        ax.set_xlabel('iteration')
        ax.set_ylabel('loss')
        
        plt.suptitle('loss')
        plt.savefig(f"./result/linear_classification/loss.png")
        
    def plotting_2d(self, idx=-1):
        fig = plt.figure(figsize = (10,7))
        ax1 = fig.add_subplot(1, 2, 1)
        ax2 = fig.add_subplot(1, 2, 2)
        
        good_data = self.x_data[self.y_data > 0]
        bad_data = self.x_data[self.y_data <= 0]
        
        ax1.plot(good_data[:,0], self.y_data[self.y_data > 0], linestyle='', color='b', marker='o', label='actual')
        ax1.plot(bad_data[:,0], self.y_data[self.y_data <= 0], linestyle='', color='r', marker='o', label='actual')
        
        # print(self.x_data[:,0].shape, self.W_list[0].shape)
        ax1.plot(self.x_data[:,0], self.x_data[:,0] * self.W_list[0], label='pred')
        ax1.set_xlabel('Quiz-1 Score')
        ax1.set_ylabel('is-great')
        
        ax2.plot(good_data[:,1], self.y_data[self.y_data > 0], linestyle='', color='b', marker='o', label='actual')
        ax2.plot(bad_data[:,1], self.y_data[self.y_data <= 0], linestyle='', color='r', marker='o', label='actual')
        
        
        ax2.plot(self.x_data[:,1], self.x_data[:,1] * self.W_list[1], label='pred')
        ax2.set_xlabel('Quiz-2 Score')
        ax2.set_ylabel('is-great')
        
        plt.suptitle('2D result')
        plt.savefig(f"./result/linear_classification/2d/{idx}.png")
        
   

    def plotting_3d(self, idx=-1):
        fig = plt.figure(figsize = (10,7))
        ax = fig.add_subplot(111, projection='3d')
        
        print(len(self.y_data[self.y_data > 0]))
        good_data = self.x_data[self.y_data > 0]
        bad_data = self.x_data[self.y_data <= 0]
        
        ax.plot(good_data[:,0], good_data[:,1], self.y_data[self.y_data > 0], linestyle='', color='b', marker='o', label='actual')
        ax.plot(bad_data[:,0], bad_data[:,1], self.y_data[self.y_data <= 0], linestyle='', color='r', marker='o', label='actual')
        
        ax.plot(self.x_data[:,0], self.x_data[:,1], self.foward(), label='pred')
        
        ax.set_xlabel('Quiz-1 Score')
        ax.set_ylabel('Quiz-2 Score')
        ax.set_zlabel('is-great')
        
        plt.legend(loc='upper right')
        
        plt.suptitle('3D result')
        plt.savefig(f"./result/linear_classification/3d/{idx}.png")
        
    def fit(self, epoch=1000):
        for i in range(epoch):
            if i % 10 == 0:
                self.plotting_3d(i)
                self.plotting_2d(i)
            
            
            self.gradient_desent()
            print(self.W_list, self.b)
            
        self.plotting_loss()
        
        
if __name__ == '__main__':
    data = pd.read_csv("./input2.txt", sep="\t")
    x_data = data.iloc[:, :2].values
    y_data = data.iloc[:, 2].values
    print(y_data)
    
    lg = LinearClassification(x_data, y_data, 'l2')
    lg.fit(epoch=5000)
    