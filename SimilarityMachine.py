import math

DEBUG = 0
NORMAL = 1

class SimilarityMachine:
    def __init__(self, db, mode=NORMAL):
        self.db = db
        self.mode = mode
        
    def getSet(self, rowId):
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
    
    def getCountDict(self, rowId):
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
        
    def getJaccard(self, row1Id, row2Id):
        row1Set = self.getSet(row1Id)
        row2Set = self.getSet(row2Id)
        
        sumSets = row1Set & row2Set
        intersection = row1Set | row2Set
        
        jaccardSimilarity = round(len(sumSets) / len(intersection), 2)
        
        if self.mode == DEBUG:
            print(f'1번 데이터의 단어집합 : {row1Set} ({len(row1Set)}개)')
            print(f'2번 데이터의 단어집합 : {row2Set} ({len(row2Set)}개)')
            print(f'두 단어집합의 합집합 : {sumSets} ({len(sumSets)}개)')
            print(f'두 단어집합의 교집합 : {intersection} ({len(intersection)}개)')
            print(f'자카드 유사도 = {len(sumSets)} / {len(intersection)} = {jaccardSimilarity}')
        
        return jaccardSimilarity
    
    def getCosine(self, row1Id, row2Id):
        row1CountDict = self.getCountDict(row1Id)
        row2CountDict = self.getCountDict(row2Id)
        
        
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
            
            dotProducted += row1Count * row2Count
            vector1Size += row1Count ** 2
            vector2Size += row2Count ** 2
            
        print(vector1Size, vector2Size)
        vector1Size = math.sqrt(vector1Size)
        vector2Size = math.sqrt(vector2Size)
        cosineSimilarity = dotProducted / (vector1Size * vector2Size)
        
        if self.mode == DEBUG:
            # print(row1CountDict)
            print(f'1번 데이터의 단어사전 : {row1CountDict}')
            print(f'2번 데이터의 단어사전 : {row2CountDict}')
            print(f'코사인 유사도 = ({dotProducted} / {round(vector1Size, 2)} * {round(vector2Size, 2)}) = {round(cosineSimilarity, 2)}')
            
        return round(cosineSimilarity, 2)