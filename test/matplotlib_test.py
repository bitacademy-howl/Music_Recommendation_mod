from itertools import count
from math import sqrt

import matplotlib.pyplot as plt
from numpy.ma import dot, zeros, count

from modules.recommendation.similarity_functions import cosine_similarity

m1 = list()
for i in range(11):
    l1 = []
    for j in range(10):
        if i > j:
            l1.append(1)
        else:
            l1.append(0)
    m1.append(l1)

print('m1 : ', m1)
result = []
for i in range(10):
    print(m1[i].count(1))
    res = int(dot(m1[i], m1[i]))
    print(res, type(res))

print(result)

result = []
for li in m1:
    res = float(cosine_similarity(li, m1[0]))
    result.append(res)
    # 분모 0 들어가면 오류 ㄴㄴ 불능 : x/0
print(result)

a = plt.subplot()
x_plot=list(range(11))
plt.scatter(x=x_plot, y=result)

plt.show()

# cosine_similarity(m1, l2)
# print(dot(l1,l2))
# print(cosine_similarity(l1, l2))

i1 = [1,1,0]
i2 = [1,1,1]

print(dot(i1, i2))

print(m1[1])

print(type(dot([1,1], [0,0])))

print(type(sqrt(dot([1,1], [0,0]) * dot([1,1], [0,0]))))

print(type(dot([1,1], [0,0])/0))