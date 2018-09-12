import math
from numpy.ma import dot

# 유사도 지표.... 유사도를 정의하는 방법들에 대해 알아볼것
# 아래는 코사인 유사도 (cosine similarity)
def cosine_similarity(v, w):
    # dot(v, v) : cos 1 = 1
    #             각 요소의 합성곱
    #             1 만으로 이루어진 벡터일 경우 벡터 자신의 1의 갯수 반환
    #             count(1)
    # 분모 = normalize factor : math.sqrt(dot(v, v) * dot(w, w))
    # 분자 = 같은 것의 갯수...단....여기서 벡터가 서로 다를 경우 cos factor < 1 포함
    # 유사할 수록 1에 근접하고, 멀어질 수록 0에 가까워 지므로....
    # 서로 다를 수록 0에 빠르게 수렴
    return dot(v, w) / math.sqrt(dot(v, v) * dot(w, w))

def custom_similarity(v, w):
    result = dot(v, w) / math.sqrt(dot(v, v) * dot(w, w))
    return result