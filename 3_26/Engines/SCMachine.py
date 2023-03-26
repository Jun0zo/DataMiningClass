#SVMuchine.py

DEBUG = 0
NORMAL = 1

# Support, Confidence값을 계산하는 클래스
class SCMachine:
    def __init__(self, db, mode=NORMAL):
        self.db = db
        self.mode = mode

    # 규칙에 해당하는 행의 개수 계산
    def _getItemCnt(self, items, dstColumnName):
        # items: 규칙을 List 형태로 받아옴 (ex: [A,B,C])
        cnt = 0
        rows = self.db.getAllRows()
        for row in rows:
            if all(item in row[dstColumnName] for item in items):
                cnt += 1
        return cnt


    # Support 값 계산. (ex. key={우유,기저귀}, value={맥주} -> (우유,기저귀,맥주)/(N) )
    def getSupportValue(self, key, value, dstColumnName):
        # key:[A,B] -> value:[a]일때 count([A,B,a] / N)  (이 때 N은 행의 개수)
        itemCnt = self._getItemCnt([*key, *value], dstColumnName)
        N = self.db.getRowsCnt()
        supportValue = round(itemCnt / N, 2)

        # debug모드일 때만 출력
        if self.mode == DEBUG:
            keyString = ','.join([*key])
            valueString = ','.join([*value])
            itemString = ','.join([*key, *value])
            print('============= Support 값 =============')
            print(f'support({keyString} -> {valueString})')
            print(f'value값( [{itemString}] )을 만족하는 행의 개수 :', itemCnt)
            print(f'전체 행 개수 : {N}')
            print(f'support값 = {itemCnt} / {N} = {supportValue}')
            print()
        
        return supportValue
    
    # Confidence 값 계산. (ex. key={우유,기저귀}, value={맥주} -> (우유,기저귀,맥주)/(우유,기저귀) )
    def getConfidencetValue(self, key, value, dstColumnName):
        # key:[A,B] -> value:[a]일때 count([A,B,a] / [A,B])
        keyValueCnt = self._getItemCnt([*key, *value], dstColumnName)
        keyCnt = self._getItemCnt([*key], dstColumnName)
        confidenceValue = round(keyValueCnt / keyCnt, 2)
        
        # debug모드일 때만 출력
        if self.mode == DEBUG:
            keyString = ','.join([*key])
            valueString = ','.join([*value])
            itemString = ','.join([*key, *value])
            
            print('============= Confidence 값 =============')
            print(f'confidence({keyString} -> {valueString})')
            print(f'key+value값( [{itemString}] )을 만족하는 행의 개수 : {keyValueCnt}')
            print(f'value값( [{keyString}] )을 만족하는 행의 개수 :', keyCnt)
            print(f'support값 = {keyValueCnt} / {keyCnt} = {confidenceValue}')
            print()
            
        return confidenceValue
