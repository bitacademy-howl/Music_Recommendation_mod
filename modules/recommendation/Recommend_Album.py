import copy
from db_accessing.VO import Album_VO, Album_recommend_VO
from modules.natural_language.NL import NL_processor
from modules.recommendation.similarity_functions import cosine_similarity



# 아래 정의된 함수는 album이 추가될 때, 추천 리스트를 갱신하고 작성하는 과정을 포함한다.
# 외부에서는 앨범 소개 항목이 있는 항목만 비교할 것!!!!!


def make_user_interest_vector(user_interests, sample_dict):
    # unique_interests[i] 가 관심사 리스트에 존재한다면 i 번째 요소가 1이고, 존재하지 않으면 0인 벡터를 생성
    return [1 if interest in user_interests else 0
            for interest in sample_dict]

# 200 개씩 불러와서
# for 문 돌면서 하나씩 비교
#  for 문 안에서는 서로의 recVO 개체를 비교하면서
#   삽입 및 정렬

def make_recommend_list(added_Album):
    batchsize = 200
    offset = 0
    # added_Album = Album_VO()


    # 추가된 앨범의 변수 및 추천리스트 초기화
    added_Album_rec = Album_recommend_VO()
    added_Album_rec.Album_ID = added_Album.Album_ID

    added_Album_dict = NL_processor(added_Album.Description).noun_count_result
    added_Album_dict_list = list(added_Album_dict.keys())

    existing_Album_list = Album_VO.query.offset(offset).limit(batchsize).all()

    # 쿼리셋이 있다면 루프수행
    while(len(existing_Album_list) != 0):
        # batch 사이즈 만큼 돌면서 루프 수행 : 개별요소 비교
        # 리스트자나....포문 바꾸자.
        # for i in range(len(existing_Album_list)):
        for existing_Album in existing_Album_list:
            # sim 초기화
            sim = 0

            # if existing_Album_list[i].Singer_ID == added_Album.Singer_ID:
            if existing_Album.Singer_ID == added_Album.Singer_ID:
                sim += 0.3

            existing_Album_rec = Album_recommend_VO.query.filter(Album_recommend_VO.Album_ID == existing_Album.Album_ID).first()


            if existing_Album_rec is None:
                existing_Album_rec = Album_recommend_VO()
                existing_Album_rec.Album_ID = existing_Album.Album_ID


            # 분기점
            # desc 가 있을때에만 비교하여 sim에 추가하는 과정이 필요

            # 유사도 함수 자체에 null 일 경우 처리를 할 수 있지만
            # 불필요한 루프는 여기서 제거
            if existing_Album.Description is not None and added_Album.Description is not None:
                existing_Album_dict = NL_processor(existing_Album.Description).noun_count_result
                exsisting_Album_dict_list = list(existing_Album_dict.keys())
                # 딥카피 해서 dict set을 별도로 만들기 위한 ref
                # dictionary_set : 유사도 비교할 두 객체의 dict sum

                dictionary_set = copy.deepcopy(added_Album_dict_list)
                dictionary_set.extend(exsisting_Album_dict_list)

                print(added_Album_dict_list)
                print(exsisting_Album_dict_list)

                dictionary_set = list(set(dictionary_set))

                print("dict_set : ", dictionary_set)

                added_IR_Vector = make_user_interest_vector(added_Album_dict_list, dictionary_set)
                existing_IR_Vector = make_user_interest_vector(exsisting_Album_dict_list, dictionary_set)

                print(added_IR_Vector, type(added_IR_Vector))
                print(existing_IR_Vector, type(existing_IR_Vector))

                sim += cosine_similarity(added_IR_Vector, existing_IR_Vector)
            # print(sim, type(sim))

            # print(existing_Album_rec.as_values())

            existing_Album_rec_dict = existing_Album_rec.as_dict()

            if existing_Album_rec_dict is None:
                existing_Album_rec.set_dict({added_Album.Album_ID: sim})
            else:
                existing_Album_rec_dict.update()
            print(existing_Album_rec.as_dict())

########################################################################################################################
        # 삽입 / 정렬 방법 생각해볼 것!!!
        # 그냥 기존 set 추가, key로 정렬할 것인지...
        # list 비교 인덱스로 접근해서 키밸류 변경 할지...

            # print(existing_Album_rec.as_keys())
            # print(existing_Album_rec.as_values())



            # dict1 = existing_Album_rec.as_dict().
            # dict1.update({added_Album.Album_ID: sim})
            # print(dict1)
            #
            # print(dict1, dict2)

            # sorted_by_value1 = sorted(dict1.items(), key=lambda kv: kv[1])[0:2]
            # sorted_by_value2 = sorted(dict2.items(), key=lambda kv: kv[1])[0:2]

            # print(sorted_by_value1)
            # print(sorted_by_value2)

        # last condition
        offset += batchsize
        existing_Album_list = Album_VO.query.offset(offset).limit(batchsize).all()


#     sim_best3 = []
#
#     print('outerloop count: ', i)
#     NLP_noun_count_dict = NL_processor(x[i].Description).noun_count_result
#     ht_list = list(NLP_noun_count_dict.keys())
#     inner_sim_best3 = []
#     for j in range(batchsize):
#
#         if i != j:
#             inner_ht_list = list(NL_processor(x[j].Description).noun_count_result.keys())
#
#             dictionary_set = copy.deepcopy(ht_list)
#             dictionary_set.extend(inner_ht_list)
#             dictionary_set = list(set(dictionary_set))
#
#             # print("dict_set : ", dictionary_set)
#
#
#             IR_Vector_inner = make_user_interest_vector(inner_ht_list, dictionary_set)
#             IR_Vector_outer = make_user_interest_vector(ht_list, dictionary_set)
#             # print(IR_Vector_inner)
#             # print(IR_Vector_outer)
#             sim = cosine_similarity(IR_Vector_inner, IR_Vector_outer)
#             # print(sim)
#
#             if len(inner_sim_best3) == recommend_size:
#                 # print('if문', file=sys.stderr)
#                 for k in range(recommend_size):
#                     if inner_sim_best3[k][0] < sim:
#                         inner_sim_best3[k] = [sim, x[j]]
#                         inner_sim_best3.sort(key = lambda element : element[0])
#                         break
#                         # print(inner_sim_best3)
#             else:
#                 # print('else 문', file=sys.stderr)
#                 inner_sim_best3.append([sim, x[j]])
#                 inner_sim_best3.sort(key = lambda element : element[0])
#                 # print(inner_sim_best3)
#
#     sim_best3.append(inner_sim_best3)
#     # print(inner_sim_best3, file=sys.stderr)
#
# for res_i in range(batchsize):
#     print(x[res_i].Album_Title, "'s recomend Album is : \n\t")
#     rec_list = []
#     for i in range(len(sim_best3[res_i])):
#         print(">>> [{0}] {1} : {2} \n\t".format(sim_best3[res_i][i][0], sim_best3[res_i][i][1].Album_ID, sim_best3[res_i][i][1].Album_Title, file=sys.stderr))
#         dict_result = {"ID": sim_best3[res_i][i][1].Album_ID, "Title": sim_best3[res_i][i][1].Album_Title,"similarity": sim_best3[res_i][i][0]}
#         rec_list.append(dict_result)
#         recommended_list_to_json(rec_list)

added_Album = Album_VO.query.filter(Album_VO.Album_ID == 1).first()
print(added_Album)
make_recommend_list(added_Album)