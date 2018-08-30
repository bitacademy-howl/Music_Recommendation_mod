from modules.User_Datasets.user_dataset import users_interests
from modules.recommendation.User_based_CF import user_based_suggestions
from modules.recommendation.pop_item_based import most_popular_new_interest


def DM_():
    # col.crawling_mnet_week_chart()
    # print(user_based_suggestions(0))
    # print(user_based_suggestions(0))
    #
    # print(user_based_suggestions(1))
    # print(user_based_suggestions(2))
    # print(user_based_suggestions(3))
    # print(user_based_suggestions(5))
    # print(user_based_suggestions(10))
    # print(user_based_suggestions(40))

    return

def DM_1():
    print("user no.1 's recommendation result : ", user_based_suggestions(0))
    suggestions = most_popular_new_interest(users_interests[1], 5)
    print("Item_based_recommendation : ", suggestions)