import numpy as np

def mse(eval, target):
    return np.sum((eval - target) ** 2 / eval.shape[0])

def l1(vectors):
    return np.sum(np.abs(vectors))

def l2(vectors):
    return np.sqrt(np.sum(vectors ** 2))

import numpy as np

def cross_entropy(eval, target):
    epsilon = 1e-7
    eval = np.clip(eval, epsilon, 1.0 - epsilon)
    loss = - (target * np.log(eval))
    avg_loss = np.mean(loss)
    return avg_loss


class Lasso:
    def __init__(self, lambda_value=0.5):
        self.lambda_value = lambda_value
        
    def __call__(self, eval, target, W_list):
        return mse(eval, target) + (self.lambda_value / 2) * l1(W_list)
    
class Ridge:
    def __init__(self, lambda_value=0.5):
        self.lambda_value = lambda_value
        
    def __call__(self, eval, target, W_list):
        return mse(eval, target) + (self.lambda_value / 2) * l2(W_list)
    
class CE:
    def __call__(self, eval, target):
        return cross_entropy(eval, target)