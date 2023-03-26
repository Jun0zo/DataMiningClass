# DistanceMachine.py

import math
from .Types.DB import DB

DEBUG = 0
NORMAL = 1

class DB:
    def __init__(self):
        self.a = 10
        self.b = 10

class DistanceMachine:
    def __init__(self, db: DB, mode: int = NORMAL) -> None:
        '''
            constructor
            Args:
                db (DB) : 데이터가 들어간 DB class
                mode (int) : [debug, normal] 모드 선택
        '''
        self.db = db
        self.mode = mode
    
    def getL2Norm(self, row1Id: str, row2Id: str) -> float:
        '''
        유클리드 거리를 return하는 함수
            Args:
                row1Id (str) : 비교대상 1번 key값
                row2Id (str) : 비교대상 2번 key값
            Returns:
                norm2Value (float) : norm1(유클리드 거리)값
        '''
        row1 = self.db.getRow(row1Id)
        row2 = self.db.getRow(row2Id)
        
        norm2Value = 0
        columnNames = self.db.getAllColumns(except_pk=True)
        # norm1 = ||row1 - row2|| 
        # = ( row1[column1] - row1[column2] )^2 + ( row2[column1] - row2[column2] )^2 + ....
        for columnName in columnNames:
            norm2Value += (row1[columnName] - row2[columnName])**2
        
        norm2Value = round(math.sqrt(norm2Value), 2)
        return norm2Value
    
    
    def getL1Norm(self, row1Id: str, row2Id: str) -> float:
        '''
        맨하튼 거리를 return하는 함수
            Args:
                row1Id (str) : 비교대상 1번 key값
                row2Id (str) : 비교대상 2번 key값
            Returns:
                norm1Value (float) : norm1(맨하튼 거리)값
        '''
        row1 = self.db.getRow(row1Id)
        row2 = self.db.getRow(row2Id)
        
        norm1Value = 0
        columnNames = self.db.getAllColumns(except_pk=True)
        # norm1 = ||row1 - row2|| (1) 
        # = | row1[column1] - row1[column2] | + | row2[column1] - row2[column2] | + ....
        for columnName in columnNames:
            norm1Value += abs(row1[columnName] - row2[columnName])
        
        return norm1Value