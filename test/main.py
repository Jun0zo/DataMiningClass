import math
ITERNUM = 5

data = [
    [1,3],
    [2,2],
    [2,3],
    [4,4],
    [4,5],
    [5,4],
]

def getL2(vector1, vector2):
    return math.sqrt(sum([(v1_feature-v2_feature)**2 for v1_feature, v2_feature in zip(vector1, vector2)]))

def clustering(K):
    centroids = [[1,2], [4,5]]
    clusters = [[] for _ in range(K)]
    for vector in data:
        min_centroid_idx = min(range(K), key= lambda i : getL2(centroids[i], vector))
        clusters[min_centroid_idx].append(vector)
        
    # for cluster in clusters:
    #     for vector in zip(*cluster)

def jaccard(s1, s2):
    
    set1 = set(s1)
    set2 = set(s2)
    
    intersection = set.intersection(set1, set2)
    union = set.union(set1, set2)
    print(intersection)
    print(union)
    print(len(intersection) / len(union))

def cosine(s1, s2):
    union = set.union(set(s1), set(s2))
    
    dot_product = sum([s1.count(c) * s2.count(c) for c in union])
    norm1 = math.sqrt(sum([s1.count(c) ** 2 for c in set(s1)]))
    norm2 = math.sqrt(sum([s2.count(c) ** 2 for c in set(s2)]))
    return dot_product / (norm1 * norm2)
    
    
    
    
def cosine2(s1, s2):
    set1, set2 = set(s1), set(s2)
    union = set.union(set1, set2)
    
    dot_product = sum([s1.count(c) * s2.count(c) for c in union])
    norm1 = math.sqrt(sum(s1.count(c)**2 for c in set1))
    norm2 = math.sqrt(sum(s2.count(c)**2 for c in set2))
    cosine_sim = dot_product / (norm1 * norm2)
    return cosine_sim

def support(data, X, Y):
    union_cnt = sum([set(X+Y).issubset(vector) for vector in data])
    all_cnt = len(data)
    return union_cnt / all_cnt

def confidence(data, X, Y):
    union_cnt = sum([set(X+Y).issubset(vector) for vector in data])
    x_cnt = sum([set(X).issubset(vector) for vector in data])
    return union_cnt / x_cnt

s1 = "영희는 익산역에 도착하여 ktx를 타고 용산역에 도착하였다. 그리고 전철을 타고 김포공항에 도착하여 제주도행 항공권을 예매하였다."
s2 = "영희는 익산역에 도착하여 ktx를 타고 용산역에 도착하였다. 그리고 전털을 타고 김포공항에 도착하여 제주도행 항공권을 예매하였다."

# jaccard(s1, s2)

# cosine_sim = cosine(s1, s2)
# print(cosine_sim)
# cosine_sim = cosine2(s1, s2)
# print(cosine_sim)


data = [['a','b','c'], ['a','d'],['b','c','d'], ['b','c']]
val = support(data, ['b'], ['c'])
print(val)

val = confidence(data, ['b'], ['c'])
print(val)