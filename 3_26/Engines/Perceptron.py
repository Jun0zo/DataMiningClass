# Perceptron.py

DEBUG = 0
NORMAL = 1

class Perceptron:
    # 가중치와 임계값을 설정
    def __init__(self, weights=[], theta=0.5, mode=NORMAL):
        self.weights = weights
        self.theta = theta
        self.mode = mode
        
    # 퍼셉트로 순전파 (값을 받아서 가중합 계산한 값을 output으로 return)
    def forward(self, inputs):
        if len(inputs) != len(self.weights):
            print('가중치값 개수와 입력값 개수가 일치하지 않습니다!' )
            return None
        
        total = 0
        # 가중합 계산 sum(n번째 가중치 * n번째 Input 값)
        for inputValue, weightValue in zip(inputs, self.weights):
            if self.mode == DEBUG:
                print(f'({inputValue} * {weightValue}) = {inputValue * weightValue}')
            total += inputValue * weightValue
        
        # 임계값에 따라 [0,1] 출력
        if total > self.theta:
            if self.mode == DEBUG:
                print(f'위 계산의 총합({total}) > 임계값({self.theta}). 따라서 출력값은 1')
            return 1
        else:
            if self.mode == DEBUG:
                print(f'위 계산의 총합({total}) < 임계값({self.theta}). 따라서 출력값은 0')
            return 0