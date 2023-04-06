from Engines.KNN import KNN
from DB.DB import DB

# 이전 시간에 사용했던 DB클래스에 저장
db = DB([
    {"name":"John", "age":35, "income":35, "card":3, "cluster":"No"},
    {"name":"Rachel", "age":22, "income":50, "card":2, "cluster":"YES"},
    {"name":"Hannah", "age":63, "income":200, "card":1, "cluster":"NO"},
    {"name":"Tom", "age":59, "income":170, "card":1, "cluster":"NO"},
    {"name":"Nellie", "age":25, "income":40, "card":4, "cluster":"YES"},
], pk_name='name')

# 벡터 공간으로 매핑 (모두 튜플로 변경)
vectors = db.convertToVectors()


# 클러스터를 구할 튜플을 선언
dst = DB([{"name":"David", "age":37, "income":50, "card":2, "cluster":""}], pk_name='name')
dst_vector = dst.convertToVectors()[0]

# print(vectors, dst_vector)

knn = KNN(vectors, 3)

# 클러스터링
result = knn.clustering(dst_vector)
# 클러스터링 결과 출력
print('result: ', result)