import math
from numpy.ma import dot

user_interest_matrix = [[1,1,0,0,0,0],
                        [1,0,1,1,0,0],
                        [0,0,1,1,0,1],
                        [1,1,1,0,1,0]]
def cosine_similarity(v, w):
    return dot(v, w) / math.sqrt(dot(v, v) * dot(w, w))

user_similarities = [[cosine_similarity(interest_vector_i, interest_vector_j)
                      for interest_vector_j in user_interest_matrix]
                     for interest_vector_i in user_interest_matrix]

print(user_similarities)

