from random import randint

import numpy
import pandas
import os

# user data 는 비정형일 수 밖에 없다.

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

# os.chdir(r"D:\1. stark\BIT_PROJ\1. Music_Recommendation\__result__")

music_list = pandas.read_csv("__result__/mnet_weeks_100.csv")
list = music_list["title"]
list = numpy.array(list).tolist()
print(list, len(list))

users_interests = []

# print(music_list)
# print(randint(0, 244))

for user in range(50):
    songs = []
    for music_index in range(50):
        songs.append(list[randint(0, len(list)-1)])
    users_interests.append(songs)


for user_interests in users_interests:
    print(user_interests)