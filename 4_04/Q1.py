from KNN import KNN

db = [
    {"name":"John", "age":35, "income":35, "card":3, "cluster":"YES"},
    {"name":"Rachel", "age":22, "income":50, "card":2, "cluster":"NO"},
    {"name":"Ryan", "age":63, "income":200, "card":1, "cluster":"NO"},
    {"name":"James", "age":59, "income":170, "card":1, "cluster":"NO"},
    {"name":"Jack", "age":25, "income":40, "card":4, "cluster":"YES"},
    {"name":"Mitchell", "age":36, "income":75, "card":2, "cluster":"YES"},
    {"name":"Boris", "age":44, "income":6, "card":3, "cluster":"NO"},

]

dst = {"name":"Daniel", "age":37, "income":50, "card":2, "cluster":""},

knn = KNN(db)

result = knn.clustering(dst)
print('result: ', result)