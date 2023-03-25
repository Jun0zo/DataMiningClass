# DB.py

class DB:
    def __init__(self, db = [], pk_name="id"):
        self.db = db
        self.pk_name = pk_name
        
    # DB에 값 저장
    def setDB(self, db):
        self.db = db

    # DB의 열이름을 모두 return
    def getAllColumns(self, except_pk=False):
        try:
            columnNames = list(self.db[0].keys())
            if except_pk:
                columnNames.remove(self.pk_name)
            return columnNames
        except:
            print("DB가 초기화 되지 않았습니다")

    # DB의 행(레코드)을 모두 return
    def getAllRows(self):
        return self.db
    
    # 해당 ID (PK)를 가진 DB의 행(레코드)을 모두 return
    def getRow(self, pk):
        rows = self.getAllRows()
        for row in rows:
            if row.get(self.pk_name) == pk:
                return row
        return None
    
    # DB의 행(레코드)의 개수를 return
    def getRowsCnt(self):
        return len(self.db)