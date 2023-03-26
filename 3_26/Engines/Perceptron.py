# Perceptron.py

DEBUG = 0
NORMAL = 1

class Perceptron:
    '''
        Perceptron Class
        
        Perceptron은 입력 값들의 가중합 임계치에 따라 [0,1] 하나의 값으로 출력하는 노드입니다.
        분류 문제에 사용될 수 있습니다.
        
        Attributes:
            weights (list) : 가중치 리스트
            theta (float) : 임계치 설정 (임계치에 따라 output이 바뀜)
            mode (int) : [debug, normal] 모드 선택
    '''
    def __init__(self, weights: list = [], theta: float = 0.5, mode: int = NORMAL):
        self.weights = weights
        self.theta = theta
        self.mode = mode
        
    def forward(self, inputs: list) -> int:
        '''
        값을 받아서 가중합 계산한 값을 output으로 return하는 함수 (순전파 함수)
            Args:
                inputs (list) : 행을 선택하기 위한 key값
            Returns:
                output (int) : 임계치에 따라 [0,1]로 return
        '''
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