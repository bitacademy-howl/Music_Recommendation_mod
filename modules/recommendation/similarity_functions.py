import math
from numpy.ma import dot

# 유사도 지표.... 유사도를 정의하는 방법들에 대해 알아볼것
# 아래는 코사인 유사도 (cosine similarity)
def cosine_similarity(v, w):
    return dot(v, w) / math.sqrt(dot(v, v) * dot(w, w))

def custom_similarity(v, w):
    result = dot(v, w) / math.sqrt(dot(v, v) * dot(w, w))
    return result