# SimilarityMachine.py

import math

from .Types.DB import DB

DEBUG = 0
NORMAL = 1

class SimilarityMachine:
    '''
        SimilarityMachine Class
        
        SimilarityMachine은 JaccardSimilarity 값과 CosineSimilarity 계산해주는 Class입니다. 
        단어 집합 A, B가 주어졌을 때
        JaccardSimilarity(자카드 유사도)값은 n(A ∩ B) / n(A ∪ B) 으로 나타낼 수 있고 
        CosineSimilarity(코사인 유사도)값은  A * B / ||A|| * ||B|| 로 표현할 수 있습니다
        
        JaccardSimilarity는 1에 근접할 수록 높은 유사도를 나타내고
        CosineSimilaritysms 0에 근접할 수록 높은 유사도를 나타냅니다.
        
        Attributes:
            db (DB) : 데이터가 들어간 DB class
            mode (int) : [debug, normal] 모드 선택
    '''
    def __init__(self, db: DB, mode: int = NORMAL):
        self.db = db
        self.mode = mode
        
    def _getSet(self, rowId: str) -> set:
        '''
        (내부함수) 해당하는 DB 행의 모든 열에 대한 Set(집합)을 return하는 함수
            Args:
                rowId (str) : 행을 선택하기 위한 key값
            Returns:
                totalSet (set) : 모든 집합
        '''
        columnNames = self.db.getAllColumns(except_pk=True)
        
        totalSet = set()
        for columnName in columnNames:
            
            row = self.db.getRow(rowId)
            data = row[columnName]
            for words in data:
                if type(words) is not list:
                    print('리스트 형식으로 입력하세요')
                    return None
                totalSet = totalSet | set(words)
        return totalSet
    
    def _getCountDict(self, rowId: str) -> dict:
        '''
        (내부함수) 해당하는 DB 행의 모든 열에 대한 단어의 개수를 dictionary형태로 return하는 함수
            Args:
                rowId (str) : 행을 선택하기 위한 key값
            Returns:
                countDict (dict) : 단어 개수 사전
        '''
        columnNames = self.db.getAllColumns(except_pk=True)
        
        
        countDict = {}
        for columnName in columnNames:
            row = self.db.getRow(rowId)
            data = row[columnName]
            for words in data:
                if type(words) is not list:
                    print('리스트 형식으로 입력하세요')
                    return None
                for word in words:
                    if not countDict.get(word):
                        countDict[word] = 0
                    countDict[word] += 1
                
        return countDict
        
    def getJaccard(self, row1Id: str, row2Id: str) -> float:
        '''
        자카드 유사도를 return하는 함수
            Args:
                row1Id (str) : 비교대상 1번 key값
                row2Id (str) : 비교대상 2번 key값
            Returns:
                jaccardSimilarity값 (float) : 자카드 유사도 값
        '''
        row1Set = self._getSet(row1Id)
        row2Set = self._getSet(row2Id)
        
        # 교집합
        intersectionSet = row1Set & row2Set
        # 합집합
        sumSet = row1Set | row2Set
        
        # 자카드 유사도 = 교집합 / 합집합
        jaccardSimilarity = round(len(sumSet) / len(intersectionSet), 2)
        
        if self.mode == DEBUG:
            print(f'1번 데이터의 단어집합 : {row1Set} ({len(row1Set)}개)')
            print(f'2번 데이터의 단어집합 : {row2Set} ({len(row2Set)}개)')
            print(f'두 단어집합의 합집합 : {sumSet} ({len(sumSet)}개)')
            print(f'두 단어집합의 교집합 : {intersectionSet} ({len(intersectionSet)}개)')
            print(f'자카드 유사도 = {len(sumSet)} / {len(intersectionSet)} = {jaccardSimilarity}')
        
        return jaccardSimilarity
    
    def getCosine(self, row1Id, row2Id):
        '''
        코사인 유사도를 return하는 함수
            Args:
                row1Id (str) : 비교대상 1번 key값
                row2Id (str) : 비교대상 2번 key값
            Returns:
                cosineSimilarity (float) : 코사인 유사도 값
        '''
        row1CountDict = self._getCountDict(row1Id)
        row2CountDict = self._getCountDict(row2Id)
        
        # 모든 단어집합
        keySets = set(row1CountDict.keys()) | set(row2CountDict.keys())
        
        dotProducted = 0
        vector1Size = 0
        vector2Size = 0
        
        for key in keySets:
            row1Count = 0
            row2Count = 0
            if row1CountDict.get(key):
                row1Count += row1CountDict[key]
            if row2CountDict.get(key):
                row2Count += row2CountDict[key]
            
            # 내적 계산
            dotProducted += row1Count * row2Count
            # 두 백터 크기 계산
            vector1Size += row1Count ** 2
            vector2Size += row2Count ** 2
            
        vector1Size = math.sqrt(vector1Size)
        vector2Size = math.sqrt(vector2Size)
        
        # 코사인 유사도 = 두 백터의 내적 / 두 백터 크기의 곱
        cosineSimilarity = dotProducted / (vector1Size * vector2Size)
        
        if self.mode == DEBUG:
            print(f'1번 데이터의 단어사전 : {row1CountDict}')
            print(f'2번 데이터의 단어사전 : {row2CountDict}')
            print(f'코사인 유사도 = ({dotProducted} / {round(vector1Size, 2)} * {round(vector2Size, 2)}) = {round(cosineSimilarity, 2)}')
            
        return round(cosineSimilarity, 2)