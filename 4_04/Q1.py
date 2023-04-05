from Engines.KNN import KNN
from DB.DB import DB


db = DB([
    {"name":"John", "age":35, "income":35, "card":3, "cluster":"No"},
    {"name":"Rachel", "age":22, "income":50, "card":2, "cluster":"YES"},
    {"name":"Hannah", "age":63, "income":200, "card":1, "cluster":"NO"},
    {"name":"Tom", "age":59, "income":170, "card":1, "cluster":"NO"},
    {"name":"Nellie", "age":25, "income":40, "card":4, "cluster":"YES"},
], pk_name='name')
vectors = db.convertToVectors()



dst = DB([{"name":"David", "age":37, "income":50, "card":2, "cluster":""}], pk_name='name')
dst_vector = dst.convertToVectors()[0]

# print(vectors, dst_vector)

knn = KNN(vectors, 3)

result = knn.clustering(dst_vector)
print('result: ', result)