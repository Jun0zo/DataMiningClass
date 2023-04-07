from Engines.HCluster import HCluster
from DB.DB import DB

# 이전 시간에 사용했던 DB클래스에 저장
db = DB([
    {"name":"A", "size":2.5, "power":2.5},
    {"name":"B", "size":2.25, "power":2},
    {"name":"C", "size":3, "power":2},
    {"name":"D", "size":2.5, "power":1.75},
    {"name":"E", "size":0.25, "power":1},
    {"name":"F", "size":0.5, "power":0.5},
    {"name":"G", "size":0.25, "power":0.25,},
    {"name":"H", "size":-0.25, "power":0.5},
    {"name":"I", "size":-0.25, "power":-0.25,},
    {"name":"J", "size":0.25, "power":-0.5},
    {"name":"K", "size":-2, "power":-1.5},
    {"name":"L", "size":-1.5, "power":-1.75},
    {"name":"M", "size":-2.5, "power":-2},
    {"name":"N", "size":-2, "power":-2.25},
    {"name":"O", "size":-2.5, "power":-2.5},
], pk_name='name')

# 벡터 공간으로 매핑 (모두 튜플로 변경)
vectors = db.projection()

hcluster = HCluster(vectors)

# 클러스터링 2개의 집합일 때 cutoff
hcluster.clustering(vectors, 2)