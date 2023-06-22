import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

data = pd.read_csv("./input2.txt", sep='\t')
x1 = data.iloc[:, 0]
x2 = data.iloc[:, 1]
y = data.iloc[:, 2]

train_size = 0.7

np.random.seed(1801570)

num_train = int(x1.shape[0] * train_size)

train_index_list = np.random.choice(x1.shape[0], num_train, replace=False)
test_index_list = np.setdiff1d(range(x1.shape[0]), train_index_list)

x1_train = x1.loc[list(train_index_list)]
x2_train = x2.loc[list(train_index_list)]
y_train = y[list(train_index_list)]

x1_test = x1.loc[test_index_list]
x2_test = x2.loc[test_index_list]
y_test = y[test_index_list]

def gradientDescent(w1, w2, b):
    global loss
    global lambda_value

    lr = 0.0001
    n = len(x1_train)
    
    y_pred = w1 * x1_train + w2 * x2_train + b

    
    
    dw1 = np.sum( (y_pred - y_train) * 2 * x1_train ) / n
    dw2 = np.sum( (y_pred - y_train) * 2 * x2_train ) / n
    db = np.sum( (y_pred) - y_train * 2 ) / n
    
    # L2 정규화
    loss_value = (y_pred - y_train) ** 2 + (lambda_value / 2) * np.sum(np.square(dw1))
    loss.append(loss_value)
    
    # 경사하강법
    w1 -= lr * dw1
    w2 -= lr * dw2
    b -= lr * db

    print(w1, w2, b)
    
    return w1, w2, b

def draw(w1, w2, b):
    fig = plt.figure(figsize = (10, 7))
    ax = fig.add_subplot(111, projection='3d')
    
    x1_good = x1_test[ w1 * x1_test + w2 * x2_test + b - y_test < 0 ]
    x2_good = x2_test[ w1 * x1_test + w2 * x2_test + b - y_test < 0 ]
    y_good = y_test[ w1 * x1_test + w2 * x2_test + b - y_test < 0 ]
    
    x1_bad = x1_test[ w1 * x1_test + w2 * x2_test + b - y_test >= 0 ]
    x2_bad = x2_test[ w1 * x1_test + w2 * x2_test + b - y_test >= 0 ]
    y_bad = y_test[ w1 * x1_test + w2 * x2_test + b - y_test >= 0 ]
    
    ax.plot(x1_test, x2_test, w1 * x1_test + w2 * x2_test + b, label='linear classification model')

    ax.plot(x1_good, x2_good, y_good, linestyle='none', marker='o', color='red', label='good')

    ax.plot(x1_bad, x2_bad, y_bad, linestyle='none', marker='o', color='blue', label='bad')

    plt.legend(loc='upper right')
    
    plt.show()
    
    plt.figure()
    plt.plot(range(len(loss)), loss)
    print("loss: ", loss[-1])
    plt.show()

w1 = random.random()
w2 = random.random()
b = 1

loss = []
learning_rate = 0.00001
epoch = 1000

lambda_value = 0.5

for i in range(epoch):
    w1, w2, b = gradientDescent(w1, w2, b)
    if i % (epoch / 10) == 0:
        print(loss[i])
        
    if i == epoch - 1:
        print( "y = %f * x1 + %f * x2 + %f" % (w1, w2, b) )
        draw(w1, w2, b)