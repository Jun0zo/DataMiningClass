import math

ITERCNT = 1
K = 3
data = [
    [35,35,3],
    [22,50,2],
    [63,200,1],
    [59,170.1],
    [25,40,4],
]
clusters = [0,1,0,0,1]
new_vector = [37,50,2]

def getL2(v1, v2):
    return math.sqrt(sum((x-y)**2 for x, y in zip(v1, v2)))

distance_list = sorted([(getL2(vector, new_vector), clusters[vector_idx]) for vector_idx, vector in enumerate(data)])[:K]
print(distance_list)