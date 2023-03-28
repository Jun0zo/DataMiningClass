# s1= 'abcde'
# s2 ='xabzdey'

class EditDistance():
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        # 편집거리를 저장할 변수
        self.memory = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
        # 편집과정 추적전용 변수 (각각 왼쪽, 왼쪽위, 위쪽을 나타냄)
        self.traces = {'left':[], 'left_up':[], 'up':[]}
        
    # 편집거리 계산하는 함수
    def getDistance(self):
        return self._editDistance(self.str1, self.str2)
    
    # 편집과정을 추적하는 함수
    def getTrace(self):
        # self.traces 변수 초기화
        self.traces = {'left':[], 'left_up':[], 'up':[]}
        position = len(self.str1), len(self.str2)
        
        # 초기 위치에서 함수 시작
        self._tracing(position, True)
        print()
        
        # self.traces에 저장된 각 변경된 알파벳들을 순서대로 출력한다.
        for direction, trace in self.traces.items():
            if direction == 'left':
                print(f'삭제 연산 {len(trace)}번 : ', end='')
                for word in trace:
                    print(f'delete {word}', end=' ')
                print()
            if direction == 'left_up':
                print(f'대체 연산 {len(trace)}번 : ', end='')
                for word1, word2 in trace:
                    print(f'{word1} -> {word2}', end=', ')
                print()
            if direction == 'up':
                print(f'삽입 연산 {len(trace)}번 : ', end='')
                for word in trace:
                    print(f'insert {word}', end=' ')
                print()
            
    # 재귀함수로 구현한 편집과정 구하는 함수
    def _tracing(self, position, is_first=False):
        i, j = position
        if (i<0 or j<0): return
        memory = self.memory
         # 왼쪽, 왼쪽위, 위쪽을 저장하는 방향과 각각의 편집거리
        directions = [(i-1, j), (i-1, j-1), (i, j-1)]
        distances = [memory[i-1][j], memory[i-1][j-1], memory[i][j-1]]
        
        # 각 방향에 존재하는 편집거리의 최소값과 위치를 구하는 과정
        min_distance = min(distances)
        min_idx = distances.index(min_distance)
        
        # 최소값이 위치한 편집거리 위치로 이동
        next_position = directions[min_idx]
        self._tracing(next_position)
        
        # 각 방향(왼쪽, 왼쪽위, 위쪽)에 대해 변경된 알파벳을 배열에 넣는다
        print(f'E[{i} {j}]', end='' if is_first else ' -> ')
        if memory[i][j] > min_distance:
            cur_chr = self.str1[i - 1]
            if min_idx == 0: # 왼쪽
                next_chr = self.str2[j+1]
                self.traces['left'].append(next_chr)
            elif min_idx == 1: # 왼쪽위
                next_chr = self.str2[j-1]
                self.traces['left_up'].append((cur_chr, next_chr))
            elif min_idx == 2: # 위쪽
                next_chr = self.str1[i+1]
                self.traces['up'].append(next_chr)
                
    # 재귀함수로 구현한 편집거리 함수
    def _editDistance(self, s1, s2):
        s1_len, s2_len = len(s1), len(s2)
        
        # 이미 저장된 값이 있으면 바로 반환 (이 부분이 없으면 많이 느려지는 것 같다)
        if self.memory[s1_len][s2_len]:
            return self.memory[s1_len][s2_len]
        
        # 문자열s1이 빈 문자열이면 문자열s2의 길이를 반환
        # (빈 문자열인 s1에서 s2로 만드는 방법은 s2의 길이만큼 삽입하는 것이기 때문)
        if s1_len == 0:
            self.memory[s1_len][s2_len] = s2_len
            return s2_len
        if s2_len == 0:
            self.memory[s1_len][s2_len] = s1_len
            return s1_len
        
        # 현재 s1='abc', s2='abcd'일 때 
        # editDistance('ab', 'abcd'), editDistance('abc', 'abc'), editDistance('ab', 'abc')의 최소값을 구한다.
        self.memory[s1_len][s2_len] = min(
            self._editDistance(s1[:-1], s2) + 1, # 삭제
            self._editDistance(s1, s2[:-1]) + 1, # 추가
            self._editDistance(s1[:-1], s2[:-1]) + (0 if s1[-1] == s2[-1] else 1) # 치환
        )
        
        # 자신을 호출했던 함수로 return
        return self.memory[s1_len][s2_len]

editDistance = EditDistance("azced", "abcdef")
distance =  editDistance.getDistance()
print(distance)
editDistance.getTrace()