from Engines.KMeans import KMeans
from DB.DB import DB

db = DB([
    {"name":"a", "age":1, "income":3,},
    {"name":"b", "age":2, "income":2, },
    {"name":"c", "age":2, "income":3, },
    {"name":"d", "age":4, "income":4, },
    {"name":"e", "age":4, "income":5, },
    {"name":"f", "age":5, "income":4, },
], pk_name="name")

vectors = db.convertToVectors()


kmeans = KMeans(vectors, 2)
kmeans.clustering()