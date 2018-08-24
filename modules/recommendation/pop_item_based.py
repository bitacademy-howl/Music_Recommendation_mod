########################################################################################################################
# user interest 카운팅!!!!!
########################################################################################################################

from collections import Counter
from modules.User_Datasets import user_dataset as us
from modules.User_Datasets.user_dataset import users_interests

popular_interests = Counter(interest
                          for user_interests in users_interests
                          for interest in user_interests).most_common()

print(popular_interests)

# 이런 형태를 가질 시 객체를 하나하나 뽑아내서 순차적으로 view 단에 append 하면 됨
# 자동으로 정렬까지 되어있다.

# for pop_item in popular_interests:
#     print(pop_item[0])

# 아래는 사용자가 관심사에 적지 않은 항목을 추천해주는 과정
def most_popular_new_interest(user_interests, max_results=5):
    suggestions = [(interest, frequency) for interest, frequency in popular_interests
                   if interest not in user_interests]
    return suggestions[:max_results]

suggestions = most_popular_new_interest(users_interests[1], 5)
print("most_popular_new_interest : ", suggestions)