DEBUG = 0
NORMAL = 1

class Perceptron:
    def __init__(self, weights=[], mode=NORMAL, theta=0.5):
        self.weights = weights
        self.mode = mode
        self.theta = theta
        
    def forward(self, inputs):
        if len(inputs) != len(self.weights):
            print('가중치값 개수와 입력값 개수가 일치하지 않습니다!' )
            return None
        
        total = 0
        for inputValue, weightValue in zip(inputs, self.weights):
            if self.mode == DEBUG:
                print(f'({inputValue} * {weightValue}) = {inputValue * weightValue}')
            total += inputValue * weightValue
        
        if total > self.theta:
            if self.mode == DEBUG:
                print(f'위 계산의 총합({total}) > 임계값{self.theta}. 따라서 출력값은 1')
            return 1
        else:
            if self.mode == DEBUG:
                print(f'위 계산의 총합({total}) < 임계값{self.theta}. 따라서 출력값은 0')
            return 0