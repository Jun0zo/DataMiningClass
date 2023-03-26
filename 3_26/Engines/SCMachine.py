# SCMachine.py

from .Types.DB import DB

DEBUG = 0
NORMAL = 1

# Support, Confidence값을 계산하는 클래스
class SCMachine:
    '''
        SCMachine Class
        
        SCMachine은 Support값과 Confidence값을 계산해주는 Class입니다. 
        항목 X, Y가 주어졌을 때
        Support(지지도)값은 n(X ∪ Y) / N 으로 나타낼 수 있고 (N은 전체 거래수)
        Confidence(신뢰도)값은 n(X∪Y) / n(X) 로 표현할 수 있습니다
        
        Attributes:
            db (DB) : 데이터가 들어간 DB class
            mode (int) : [debug, normal] 모드 선택
    '''
    def __init__(self, db: DB, mode: int = NORMAL):
        self.db = db
        self.mode = mode

    def _getItemCnt(self, items: list, dstColumnName: str) -> int:
        '''
        (내부함수) 입력한 규칙이 존재하는 행(row)의 개수를 return하는 함수
            Args:
                items (list) : 규칙을 list형태로 입력
                dstColumnName (str) : 분석할 열(column)의 이름
            Returns:
                cnt (int) : 해당 규칙이 존재하는 행의 개수
        '''
        cnt = 0
        rows = self.db.getAllRows()
        # 해당 규칙이 DB에 있으면 카운트 + 1
        for row in rows:
            if all(item in row[dstColumnName] for item in items):
                cnt += 1
        return cnt


    # Support 값 계산.
    def getSupportValue(self, key: list, value: list, dstColumnName: str) -> float:
        '''
        입력한 key, value(규칙)로 support값을 계산하여 supportValue를 Return하는 함수
        (ex. key={우유,기저귀}, value={맥주} -> (우유,기저귀,맥주)/(N) )
            Args:
                key (list) : key 규칙을 list형태로 입력
                value (list) : value 규칙을 list형태로 입력
                dstColumnName (str) : 분석할 열(column)의 이름
            Returns:
                supportValue (float) : support값
        '''
        # key:[A,B] -> value:[a]일때 count([A,B,a] / N)  (이 때 N은 전체 행의 개수)
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
    
    def getConfidencetValue(self, key: list, value: list, dstColumnName: str) -> float:
        '''
        입력한 key, value(규칙)로 confidence값을 계산하여 confidenceValue를 Return하는 함수
        (ex. key={우유,기저귀}, value={맥주} -> (우유,기저귀,맥주)/(우유,기저귀) )
            Args:
                key (list) : key 규칙을 list형태로 입력
                value (list) : value 규칙을 list형태로 입력
                dstColumnName (str) : 분석할 열(column)의 이름
            Returns:
                confidenceValue (float) : confidence값
        '''
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
