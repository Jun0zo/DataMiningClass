from KMEANS import KMeans

db = [
    {"name":"a", "age":1, "income":3,},
    {"name":"b", "age":2, "income":2, },
    {"name":"c", "age":2, "income":3, },
    {"name":"d", "age":4, "income":4, },
    {"name":"e", "age":4, "income":5, },
    {"name":"f", "age":5, "income":4, },

]


kmeans = KMeans(db, 2)

kmeans.clustering()