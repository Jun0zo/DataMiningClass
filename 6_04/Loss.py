import numpy as np

def mse(eval, target):
    return np.sum((eval - target) ** 2 / eval.shape[0])

def l1(vectors):
    return np.sum(np.abs(vectors))

def l2(vectors):
    return np.sqrt(np.sum(vectors ** 2))

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