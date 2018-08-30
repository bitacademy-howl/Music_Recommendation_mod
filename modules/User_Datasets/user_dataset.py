from random import randint

import numpy
import pandas
import os

# user data 는 비정형일 수 밖에 없다.
# user data를 정해진 size 로 고정하지 않는다면, 이 말은 Nosql 사용은 필연적이라는 것!
# fix 할 경우 데이터에 상관없이 null 을 허용할 수도... size 범위를 벗어나면 FIFO,
# 혹은 적게 열람한 순서로 빼내는 방법들을 적용할 수도 있겠다..

#

# users_interests = [["Hadoop", "Big Data", "HBase", "Java", "Spark", "Storm", "Cassandra"],
#                    ["NoSQL", "MongoDB", "Cassandra", "HBase", "Postgres"],
#                    ["Python", "scikit-learn", "scipy", "numpy", "statsmodels", "pandas"],
#                    ["R", "Python", "statistics", "regression", "probability"],
#                    ["machine learning", "regression", "decision trees", "libsvm"],
#                    ["Python", "R", "Java", "C++", "Haskell", "programming languages"],
#                    ["statistics", "probability", "mathmatics", "theory"],
#                    ["machine learning", "scikit-learn", "Mahout", "neural networks"],
#                    ["neual networks", "deep learning", "Big Data", "artifical intelligence"],
#                    ["Hadoop", "Java", "MapReduce", "Big Data"],
#                    ["statistics", "R", "statsmodels"],
#                    ["C++", "deeplearning", "artificial intelligence", "probability"],
#                    ["pandas", "R", "Python"],
#                    ["databases", "HBase", "postgres", "MySQL", "MongoDB"],
#                    ["libsvm", "regression", "support vector machines"]]

music_list = pandas.read_csv("__result__/mnet_weeks_100.csv")
list = music_list["title"]
list = numpy.array(list).tolist()
print(list, len(list))

users_interests = []

for user in range(50):
    songs = []
    for music_index in range(50):
        songs.append(list[randint(0, len(list)-1)])
    users_interests.append(songs)

for user_interests in users_interests:
    print(user_interests)