from collections import defaultdict
from modules.User_Datasets.user_dataset import users_interests
from test.ss_test import cosine_similarity

unique_interests = sorted(list({interest
                                for user_interests in users_interests
                                for interest in user_interests}))

# 각 사용자의 관심사 벡터 생성 (다차원 벡터의 차수는 unique_interests 와 동일
# 사용자가 해당 관심사를 가지고 있다면 1, 그렇지 않으면 0인 값을 갖는 벡터로 사용자의 관심사를 나타낸다.
def make_user_interest_vector(user_interests):
    # unique_interests[i] 가 관심사 리스트에 존재한다면 i 번째 요소가 1이고, 존재하지 않으면 0인 벡터를 생성
    return [1 if interest in user_interests else 0
            for interest in unique_interests]

# vector_of_1 = make_user_interest_vector(users_interests[3])
# print(vector_of_1)


########################################################################################################################
# more researching.............................................................................
# map : 지정된 리스트나 튜플을 지정된 함수로 처리하는 함수.
# 사용 : map([함수명], [데이터])
########################################################################################################################
# user_interest_matrix = map(make_user_interest_vector, users_interests)
#
# for i in user_interest_matrix:
#     print(i, type(i))

user_interest_matrix = []
for i in range(len(users_interests)):
    user_interest_matrix.append(make_user_interest_vector(users_interests[i]))

user_similarities = [[cosine_similarity(interest_vector_i, interest_vector_j)
                      for interest_vector_j in user_interest_matrix]
                     for interest_vector_i in user_interest_matrix]


# for i in user_similarities:
#     print(i)
# print(user_similarities[13][0])


# sorted 함수 찾아볼 것!!!!!

# 사용자의 관심사를 모든 사용자와의 유사도를 구하여, 튜플리스트로 리턴
def most_similar_users_to(user_id):
    pairs = [(other_user_id, similarity)
             for other_user_id, similarity in enumerate(user_similarities[user_id])
             if user_id != other_user_id and similarity > 0]
    return sorted(pairs, key=lambda similarity : similarity[1], reverse = True)

# msut1 = most_similar_users_to(0)
# print(msut1)
#
# msut2 = most_similar_users_to(1)
# print(msut2)

def user_based_suggestions(user_id, include_current_interests=False):
    # 모든 유사도를 더함
    suggestions = defaultdict(float)
    for other_user_id, similarity in most_similar_users_to(user_id):
        for interest in users_interests[other_user_id]:
            suggestions[interest] += similarity

    # 정렬된 list로 변환
    suggestions = sorted(suggestions.items(), key=lambda weight : weight[1], reverse=True)

    # (원한다면) 이미 관심사로 표시한 것은 제외한다.
    if include_current_interests:
        return suggestions
    else:
        return [(suggestion, weight)
                for suggestion, weight in suggestions
                if suggestion not in users_interests[user_id]]

print(user_based_suggestions(0))
