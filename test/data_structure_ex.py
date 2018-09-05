from modules.recommendation.similarity_functions import similarity_howl

list1 = ['날', '가시나', '새', '음악', '때', '고혹', '동시', '파격적', '선', '미가', '곡', '발표', '막강', '프로듀서', '포진', '블랙', '레이블', '과', '공동', '작업', '야심', '준비', '동양적', '분위기', '사운드', '테마', '감각', '적인', '베이스', '라인', '세련', '멜로디', '선미', '절제', '섹시', '미', '완성', '지금', '보컬', '솔로', '아티스트', '성숙', '역량', '호기심', '유발', '제목', '의미', '내포', '중의', '표현', '꽃', '가시', '모습', '이별', '앞', '뇌', '임인', '가사', '한', '우리말', '무리', '뜻', '지점', '감성', '의', '협업', '프로', '작사', '참여', '몰입', '발매', '스페셜', '디', '무한', '잠재력', '감수성', '여성', '존재', '감', '본격적', '시작', '작곡', '편곡']
list2 = ['눈빛', '맘', '불씨', '재', '남', '시간', '약', '아픔', '꽃', '나의', '향', '길', '원해', '모두', '바보', '날', '가시나', '약속', '고개', '가시', '모습', '미안', '마', '지금', '내가', '당장', '생각']

list3 = list1.copy()

list3.extend(list2)

list1.sort()
list2.sort()
sample_dict = list(set(list3))
sample_dict.sort()


print(sample_dict, "\n", list1, "\n", list2, "\n")

def make_user_interest_vector(user_interests, sample_dict):
    # unique_interests[i] 가 관심사 리스트에 존재한다면 i 번째 요소가 1이고, 존재하지 않으면 0인 벡터를 생성
    return [1 if interest in user_interests else 0
            for interest in sample_dict]

interestV_1 = make_user_interest_vector(list1, sample_dict)
print(interestV_1)
interestV_2 = make_user_interest_vector(list2, sample_dict)
print(interestV_2)

sim = similarity_howl.cosine_similarity(interestV_1, interestV_2)

print(sim)

