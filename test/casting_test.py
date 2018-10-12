import json
import os

# str1 = '01'
# int1 = int(str1)
# print(int1)
#
# list1 = ['2000', '01', '02']
# t1 = tuple(list1)
# list2 = list(map(lambda x:int(x), list1))
#
# print(type(list2), type(list2[0]), type(list2[1]), type(list2[2]))
# print(list2[0],list2[1],list2[2])
#
#
#
# # 반드시 쌍따옴표...key
# str = u'{"rec1":123123,"rec2":33212,"rec3":313455}'
# dict1 = json.loads(str)
# print(dict1, type(dict1))
#
#
# str = u'{"rec1":[{"d":123123},1,2,3],"rec2":33212,"rec3":313455}'
# dict1 = json.loads(str)

#
# print(dict1, type(dict1))
# print(dict1.keys())
# for s in dict1.keys():
#     print(dict1.get(s), type(dict1.get(s)))
#     if isinstance(dict1.get(s), list):
#         for x in dict1.get(s):
#
#             if isinstance(x, dict):
#                 print("#################################")
#                 print(x, type(x))
#                 print("#################################")
#
#
# print(dict1)
# print(dict1.get("1"))

# str1 = "asdfasdfasdfasdf"
# print(str1.__iter__())

# for dkey in dict1.keys():
#     if isinstance(dict1.get(dkey), (int, str, float)):
#         print(dkey, "'s value is Basic Type: ",type(dict1.get(dkey)))
#         # print(dict1.get(dkey).__iter__())
#     if dict1.__iter__() is None:
#         print(dkey, "'s value is Non Basic Type: ",type(dict1.get(dkey)))


# ..................................................
# .........................
# .........................
# .........................
# .........................
# .........................

dir = '__result__'
if not os.path.exists(dir):
    os.mkdir(dir)

dict1 = {
    "id" : 102929,
    1 : "dasdasd",

    "workflows": [{
            "workflowName": "test",
            "workflowFilename": "exampleWorkflow.json"
        }],

    "producers": [{
            "type": "kafka",
            "broker.server": "192.168.59.103",
            "broker.port": 9092,
            "topic": "logevent",
            "sync": False
    },{
        "type":"logger"
    }]
}



# 구분 : 성격                      : 사용목적                                  : 누구를 위해
# str  : 비공식적인 문자열을 출력  : 사용자가 보기 쉽게 하기 위해              : 프로그램 사용자(end user)
# repr : 공식적인 문자열을 출력    : 문자열로 객체를 다시 생성할 수 있기 위해  : 프로그램 개발자(developer)

# __repr__ 은 eval() 로 생성자를 활용하여 해당 객체를 생성할 수 있도록 정의하여야 함.


list1 = [1,2,3]
print(str(dict1), "\n",dict1.__str__())
print(dict1.__repr__())
dict3 = eval(dict1.__repr__())
print(dict3, type(dict3))

dict1_str = dict1.__repr__()







# # 데이터 로드 모듈
def recommended_list_to_json(rec_list):
    fname = '{0}/result_{1}.json'.format(dir, dict1.get("id"))
    with open(fname, mode='w', encoding='utf8') as f:
        try:
            json.dump(rec_list.__repr__(),fp=f, skipkeys=True, ensure_ascii=False)
        except Exception as e:
            print(e)
#
# recommended_list_to_json(dict1)
#

# dict 는 string으로 저장하고 json load 로 메모리에 적재할 것!
