import math

def L2(vector1, vector2):
    return math.sqrt(sum([(x-y)**2 for x,y in zip(vector1[:-1], vector2[:-1])]))


data = [
    [1,2,3,4,5, "A"],
    [13,27,33,14,85, "B"],
]
distance = L2(data[0], data[1])
print(distance)