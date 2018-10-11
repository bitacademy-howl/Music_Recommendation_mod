import copy
import os

import sys
import json

from db_accessing.VO import Album_VO
from modules.natural_language.NL import NL_processor
from modules.recommendation.similarity_functions import cosine_similarity

def make_user_interest_vector(user_interests, sample_dict):
    # unique_interests[i] 가 관심사 리스트에 존재한다면 i 번째 요소가 1이고, 존재하지 않으면 0인 벡터를 생성
    return [1 if interest in user_interests else 0
            for interest in sample_dict]

# for i in range(1, lenOfNotNULL, batchsize):
# for offs in range(1, 10, batchsize):

dir = '__recommand__'
if not os.path.exists(dir):
    os.mkdir(dir)

lenOfNotNULL = Album_VO.query.filter(Album_VO.Description != None).count()
print(lenOfNotNULL, type(lenOfNotNULL))

batchsize = 200
recommend_size = 3
def recommended_list_to_json(rec_list):
    fname = '{0}/recommand_album_{1}.json'.format(dir, x[res_i].Album_ID)
    with open(fname, mode='w', encoding='utf8') as f:
        for dict_input in rec_list:
            json.dump(dict_input,fp=f, ensure_ascii=False)
            f.write('\n')


x = Album_VO.query.filter(Album_VO.Description != None).offset(210).limit(batchsize).all()
for seg in x:
    print(seg.Album_Title)
# print(len(x), type(x))

sim_best3 = []
for i in range(batchsize):
    print('outerloop count: ', i)
    NLP_noun_count_dict = NL_processor(x[i].Description).noun_count_result
    ht_list = list(NLP_noun_count_dict.keys())
    inner_sim_best3 = []
    for j in range(batchsize):

        if i != j:
            inner_ht_list = list(NL_processor(x[j].Description).noun_count_result.keys())

            dictionary_set = copy.deepcopy(ht_list)
            dictionary_set.extend(inner_ht_list)
            dictionary_set = list(set(dictionary_set))

            # print("dict_set : ", dictionary_set)


            IR_Vector_inner = make_user_interest_vector(inner_ht_list, dictionary_set)
            IR_Vector_outer = make_user_interest_vector(ht_list, dictionary_set)
            # print(IR_Vector_inner)
            # print(IR_Vector_outer)
            sim = cosine_similarity(IR_Vector_inner, IR_Vector_outer)
            # print(sim)

            if len(inner_sim_best3) == recommend_size:
                # print('if문', file=sys.stderr)
                for k in range(recommend_size):
                    if inner_sim_best3[k][0] < sim:
                        inner_sim_best3[k] = [sim, x[j]]
                        inner_sim_best3.sort(key = lambda element : element[0])
                        break
                        # print(inner_sim_best3)
            else:
                # print('else 문', file=sys.stderr)
                inner_sim_best3.append([sim, x[j]])
                inner_sim_best3.sort(key = lambda element : element[0])
                # print(inner_sim_best3)

    sim_best3.append(inner_sim_best3)
    # print(inner_sim_best3, file=sys.stderr)

for res_i in range(batchsize):
    print(x[res_i].Album_Title, "'s recomend Album is : \n\t")
    rec_list = []
    for i in range(len(sim_best3[res_i])):
        print(">>> [{0}] {1} : {2} \n\t".format(sim_best3[res_i][i][0], sim_best3[res_i][i][1].Album_ID, sim_best3[res_i][i][1].Album_Title, file=sys.stderr))
        dict_result = {"ID": sim_best3[res_i][i][1].Album_ID, "Title": sim_best3[res_i][i][1].Album_Title,"similarity": sim_best3[res_i][i][0]}
        rec_list.append(dict_result)
        recommended_list_to_json(rec_list)





# print('batch : {0}'.format(i/batchsize))

# mat = []
# for i in range(len(x)):
#     mat.append(NL_processor(x[i].Description).all_count_result)
#     print(mat[i])
#
# print()