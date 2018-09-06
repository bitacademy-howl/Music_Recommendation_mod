from konlpy.tag import Kkma
from modules.recommendation.similarity_functions import cosine_similarity

class NL_processor:
    def noun_count(self, text):
        hash_tags = self.kkma.pos(text)
        for ht in hash_tags:
            if ht[1] == "NNG":
                if ht[0] in self.noun_count_result.keys():
                    self.noun_count_result[ht[0]] += 1
                else:
                    self.noun_count_result[ht[0]] = 1

    def all_count(self, text):
        hash_tags = self.kkma.pos(text)
        for ht in hash_tags:
            if ht[0] in self.all_count_result.keys():
                self.all_count_result[ht[0]] += 1
            else:
                self.all_count_result[ht[0]] = 1

    def __init__(self, text):
        self.all_count_result = {}
        self.noun_count_result = {}
        self.text = text
        self.kkma = Kkma()

        self.noun_count(text)
        self.all_count(text)

    def text_update(self, text):
        self.text = text
        self.noun_count(text)
        self.all_count(text)


NLP1 = NL_processor(
    '''예쁜 날 두고 ‘가시나’

새로운 음악을 선보일 때마다 고혹적인 동시에 파격적인 컨셉을 선보여 온 선미가 3년 만에 새로운 곡 ‘가시나’를 발표 했다. 이번 곡은 막강한 프로듀서들이 포진해있는 ‘더 블랙 레이블(The Black Label)’과 공동 작업을 통해 야심차게 준비한 음악으로 동양적인 분위기의 신스 사운드가 주된 테마인 곡으로 감각적인 베이스 라인에 세련된 멜로디 라인이 더해져 선미의 절제된 섹시미를 완성시킨다. 지금까지 숨겨왔던 선미의 다채로운 보컬은 솔로 아티스트로서 한층 더 성숙해진 그녀의 역량을 보여주었다.

호기심을 유발하는 곡의 제목 ‘가시나’는 세 가지 의미를 내포한 중의적인 표현으로, 이는 꽃에 돋아 난 ‘가시’처럼 ‘가시 난 내 모습이 더 깊숙이 파고들 거야’, 안타까운 이별 앞의 쓸쓸한 되뇌임인 ‘왜 예쁜 날 두고 가시나’ 등의 가사로 유려하게 음악에 녹아 들고 있다. 또한, 순 우리말 ‘가시나’에 ‘아름다운 꽃의 무리’라는 뜻이 숨겨져 있다는 지점에 이르면, 아티스트로서 선미의 깊고 예민한 감성을 마주할 수 있다.

선미와 ‘더 블랙 레이블(The Black Label)’의 협업으로 완성된 ‘가시나’는 ‘더 블랙 레이블(The Black Label)’이 프로듀싱했으며, 선미가 이들과 함께 작사에 참여해 음악에 대한 몰입도를 더욱 높였다.

이번 발매하는 스페셜 에디션 ‘가시나’는 무한한 잠재력과 예민한 감수성을 가진 선미의 여성 솔로 아티스트로서의 존재감을 본격적인 보여줄 수 있는 시작이 될 것이다., 


가시나 (Gashina)
작사 : Teddy, 선미, Joe Rhee, 24 / 작곡 : Teddy, 24, Joe Rhee / 편곡 : 24, Joe Rhee
동양적인 분위기의 신스 사운드가 주된 테마인 곡으로 감각적인 베이스 라인에 세련된 멜로디 라인이 더해져 선미의 절제된 섹시미를 완성시킨다. 
    '''
)


print(sorted(NLP1.all_count_result.items(), key=lambda freq : freq[1], reverse=True))


NLP2 = NL_processor(
    '''너의 싸늘해진 그 눈빛이
나를 죽이는 거야 
커지던 니 맘의 불씨
재만 남은 거야 왜
시간이 약인가봐 
어째 갈수록 나 약하잖아
슬픈 아픔도 
함께 무뎌지는 거야

좋아 이젠 너를 잊을 수 있게 
꽃같이 살래 나답게
Can't nobody stop me now 
no try me 

나의 향길 원해 모두가 
바보처럼 왜 너만 몰라
정말 미친 거 아냐 넌

왜 예쁜 날 두고 가시나

날 두고 떠나가시나
그리 쉽게 떠나가시나
같이 가자고 
약속해놓고 
가시나 가시나 

날카로운 날 보고 넌
고개 숙일 거야 
가시 난 내 모습이
더 깊숙이 파고들 거야 eh
이미 꺾은 거잖아 
굳이 미안해하지 마
정말 꺾인 건 지금 내가
아냐 바로 너야
좋아 이젠 너를 잊을 수 있게
꽃같이 살래 나답게
Can't nobody stop me now 
no try me 

나의 향길 원해 모두가 
바보처럼 왜 너만 몰라
정말 미친 거 아냐 넌

왜 예쁜 날 두고 가시나

날 두고 떠나가시나
그리 쉽게 떠나가시나
같이 가자고
약속 해놓고
가시나 가시나 

너는 졌고 나는 폈어
And it's over 
다시 돌아온다 해도 
지금 당장은 나 없이 
매일 잘 살 수 있을 것 같지
암만 생각해봐도 미친 거 아냐 넌

왜 예쁜 날 두고 가시나

날 두고 떠나가시나
그리 쉽게 떠나가시나
같이 가자고 
약속해놓고 
가시나 가시나'''
)

# print(NLP2.all_count_result)
# print(sorted(NLP2.all_count_result.items(), key=lambda freq : freq[1], reverse=True))
#
# print(NLP2.noun_count_result)

# print(NLP1.all_count_result)
# print(NLP1.noun_count_result)

k1 = sorted(NLP1.noun_count_result.items(), key=lambda freq : freq[1], reverse=True)
k2 = sorted(NLP2.noun_count_result.items(), key=lambda freq : freq[1], reverse=True)
print(k1, '\n', k2, '\n', type(k1))

k1 = list(NLP1.noun_count_result.keys())
k2 = list(NLP2.noun_count_result.keys())

print(k1, '\n', k2, '\n', type(k1))
cosine_similarity(k1, k2)

from modules.recommendation.similarity_functions import cosine_similarity

k3 = k1.copy()

k3.extend(k2)

sample_dict = list(set(k3))
sample_dict.sort()

print(sample_dict, "\n", k1, "\n", k2, "\n")

# def make_user_interest_vector(user_interests, sample_dict):
#     # unique_interests[i] 가 관심사 리스트에 존재한다면 i 번째 요소가 1이고, 존재하지 않으면 0인 벡터를 생성
#     return [1 if interest in user_interests else 0
#             for interest in sample_dict]
#
# interestV_1 = make_user_interest_vector(k1, sample_dict)
# print(interestV_1)
# interestV_2 = make_user_interest_vector(k2, sample_dict)
# print(interestV_2)

sim = cosine_similarity(k1, k2)

print(sim)