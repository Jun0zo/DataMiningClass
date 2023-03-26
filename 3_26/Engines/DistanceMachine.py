DEBUG = 0
NORMAL = 1

import math

class DistanceMachine:
    def __init__(self, db, mode=NORMAL):
        self.db = db
        
    # 유클리드 거리 return
    def getL2Norm(self, row1Id, row2Id):
        row1 = self.db.getRow(row1Id)
        row2 = self.db.getRow(row2Id)
        
        total = 0
        columnNames = self.db.getAllColumns(except_pk=True)
        for columnName in columnNames:
            total += (row1[columnName] - row2[columnName])**2
        
        return math.sqrt(total)
    
    # 맨하튼 거리 return
    def getL1Norm(self, row1Id, row2Id):
        row1 = self.db.getRow(row1Id)
        row2 = self.db.getRow(row2Id)
        
        total = 0
        columnNames = self.db.getAllColumns(except_pk=True)
        for columnName in columnNames:
            total += abs(row1[columnName] - row2[columnName])
        
        return total