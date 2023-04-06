from Engines.KMeans import KMeans
from DB.DB import DB

# 이전 시간에 사용했던 DB클래스에 저장
db = DB([
    {"name":"a", "age":1, "income":3,},
    {"name":"b", "age":2, "income":2, },
    {"name":"c", "age":2, "income":3, },
    {"name":"d", "age":4, "income":4, },
    {"name":"e", "age":4, "income":5, },
    {"name":"f", "age":5, "income":4, },
], pk_name="name")

# 벡터 공간으로 매핑 (모두 튜플로 변경)
vectors = db.convertToVectors()

# 클러스터링 시작
kmeans = KMeans(vectors, 2)
kmeans.clustering()