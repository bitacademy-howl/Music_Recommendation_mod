# 데이터 시작은 2009년 1월 1일부터로 한다.
# 이유 : 2007, 2008년 연간 차트 존재, but 주간 및 일간차트 존재하지 않음

from collection import collect as col
from modules.recommendation.User_based_collaborative_filtering import user_based_suggestions

if __name__ == '__main__':
    # pelicana
    # col.crawling_mnet_week_chart()
    print(user_based_suggestions(0))
    print(user_based_suggestions(0))

    print(user_based_suggestions(1))
    print(user_based_suggestions(2))
    print(user_based_suggestions(3))
    print(user_based_suggestions(5))
    print(user_based_suggestions(10))
    print(user_based_suggestions(40))