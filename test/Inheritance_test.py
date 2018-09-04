# from VO import db

# class Music_VO(db.Model):
#     Music_ID = Column(db.Integer, primary_key=True, unique=True)
#     Title = Column(db.String(100))
#     Singer = Column(db.String(100))
#     Album = Column(db.String(100))
#
#     def __init__(self):
#         pass
#
#     def __repr__(self):
#         return "<Music('%s')>" % str(self.as_dict)
#
#     def as_dict(self):
#         return {x.name: getattr(self, x.name) for x in self.__table__.columns}

from db_accessing import Music_VO, db

mv = Music_VO.query.filter_by(Singer="김건모").all()
# print(mv, type(mv))
#
# print(mv[0], type(mv[0]))
#
def innerF(mv):
    attr = mv[0].as_dict()
    return attr
#
attr = innerF(mv=mv)
print(attr)

dict1 = {'Music_ID': 24357, 'Title': '농사꾼', 'Singer': '김건모내기', 'Album': '밭갈기', 'Genre': None, 'Composer': None, 'Lyricist': None, 'Hash_Tags': None, 'Release_Date': None}
dict2 = {'Music_ID': 24357, 'Title': 'sda', 'Singer': '김건모내기', 'Album': '밭갈기', 'Genre': None, 'Composer': None, 'Lyricist': None, 'Hash_Tags': None, 'Release_Date': None}
# dict2 = {'Title': 'sda', 'Singer': '김건모내기', 'Album': '밭갈기', 'Genre': None, 'Composer': None, 'Lyricist': None, 'Hash_Tags': None, 'Release_Date': None}
dict3 = {'Music_ID': 24357, 'Title': 'li', 'Singer': '김건모내기', 'Album': '밭갈기', 'Genre': None, 'Composer': None, 'Lyricist': None, 'Hash_Tags': None, 'Release_Date': None}
dict4 = {'Music_ID': 24357, 'Title': 'last', 'Singer': '김건모내기', 'Album': '밭갈기', 'Genre': None, 'Composer': None, 'Lyricist': None, 'Hash_Tags': None, 'Release_Date': None}

list_b = [dict1, dict2, dict3, dict4]
a = mv[0]

print(a)

for k, v in a.as_dict().items():
    print(k , " : ", v)

DAO = Music_VO()
DAO.from_dict_strict(dict3)
dict_result = DAO.as_dict()
for k, v in dict_result.items():
    print(k , " : ", v)

# dict_result = mv[0].as_dict()
# for k, v in dict_result.items():
#     print(k , " : ", v)

# configure 옵션에 대해 알아볼 것!
# 세션 생성후에는 적용할 수 없음
# db.session.configure()

print(db.session.autocommit)
db.session.merge(DAO)
db.session.commit()

# 아래와 같이 session 을 통해 db 에 쿼리할 경우마다 file open 처럼 사용 가능
# with db.session.no_autoflush: <----- 이는 db 연결 시 flask 설정을 통해 적용가능
#     print(db.session.autocommit)
#     db.session.merge(DAO)
#     db.session.commit()

##############################################################################################################
# 아래는 동작하지 않는다.
# 학습이 더 필요한 내용이지만, 실제 session을 통해 얻어온 객체를 값만 바꿔서 create 객체로 사용이 불가능
# 현재로썬 그렇다..
# 아래 구문을 사용하면 객체 내 Primary-key를 변경하더라도 가져올 때의 행의 Primary-key 까지 업데이트 하려는
# 구문으로 수행되어 해당 오류가 발생한다.
# with db.session.no_autoflush:
#     print(db.session.autocommit)
    # for b in list_b:
    #     mv[0].from_dict(b)
    #     db.session.merge(mv[0])
##############################################################################################################

# print(dict1, type(dict1))
#
# class obj(object):
#     def __init__(self, d):
#         for a, b in d.items():
#             if isinstance(b, (list, tuple)):
#                setattr(self, a, [obj(x) if isinstance(x, dict) else x for x in b])
#             else:
#                setattr(self, a, obj(b) if isinstance(b, dict) else b)
#
# d = {'a': 1, 'b': {'c': 2}, 'd': ["hi", {'foo': "bar"}]}
#
# x = obj(d)
# print(x.a, x.b, x.b.c, x.d)
# print(x.d[0])
# print(x.d[1].foo)
# x.b.c
# x.d[1].foo
#
#
# class obj(object):
#     def __init__(self, d):
#         for a, b in d.items():
#             setattr(self, a, obj(b) if isinstance(b, dict) else b)
#
# d = {'a': 1, 'b': {'c': 2}, 'd': ["hi", {'foo': "bar"}]}
#
# x = obj(d)
# print(x.a, x.b, x.b.c)



############################################################################################################
# 아래 구문은 Music_VO가 상속받은 db.Model 클래스의 속성 __table__
# 상속받은 객체에서 __tablename__을 정의하면 부모객체의 __table__이 동기화 되는 것을 알 수 있다.
# 확인할 수 있듯이....call by ref 로 동작하지는 않음
# print(Music_VO.__table__, Music_VO.__table__ == Music_VO.__tablename__)

# 아래에서 확인하듯 __tablename__ 은 str....__table__은 print 시에만 __tablename__을 반환하도록 되어있는듯

print(Music_VO.__table__, type(Music_VO.__table__))
print(Music_VO.__tablename__, type(Music_VO.__tablename__))
############################################################################################################
# 즉 다시말해 위의 구조는 아래의 샘플코드와 같이 동작할 것!!
# 와 시발 재미쪙.....
# 상속 및 innerclass examples........
class model:
    __tablename__ = ""
    what = 1

    def createInner(self):
        return model.table(self)

    def __init__(self):
        self.__table__ = self.createInner()

    class table():
        def __init__(self, outer_instance):
            self.outer_instance = outer_instance

        def __str__(self):
            return self.outer_instance.__tablename__


class model2:
    what = 2

class child(model, model2):
    __tablename__ = "하이"

    ##########################################################################################################
    # 아래는 보너스
    # 아래와 같은 코드는 동작할 수 없음.....상속이란 클래스에서 이루어지고, 객체화는 자식클래스가 이루어지는것
    # 다시말해 super 는 클래스, 아래의 ch 는 객체....
    # 상속되어 obj로 메모리 올려야 값을 읽을 수 있다.
    # 그렇다면 Static 은??????~!!!!!!!
    # 좀 더 많이 해봐야 익숙해질 듯
    def getsuper_what(self):
        # 아래는 에러 super는 클래스
        # print(super.what)

        # 아래는 가능.....상속받아 생성되면 부모도 같이 생성되고 이때 생성된 부모객체(상속받은)에 대한
        # 접근은 아래와 같은 방식으로 가능
        print(model.what)
        print(model2.what)

        # super 에 있는 값을 사용하고 싶은 경우....
        # 슈퍼를 생성하고 나서야 사용가능

        print(super().what, type(super()))
        pass
#############################################################################################################
ch = child()
print(ch.__table__)

# mo = model()
# print(mo.__table__)

ch.getsuper_what()
############################################################################################################

############################################################################################################
# 곰곰이 생각해 보면 자바에서는 다중상속이란 개념이 없고, 자식 객체 생성 시 부모 클래스의 생성자를 호출하기
# 때문에 super라 하면 부모 객체(in memory) = 부모 클래스(code) = super 에 대한 혼동이 없다.

# 하지만 파이썬은 다중 상속이 가능하고, 다중상속으로 생겨나는 중복변수 등 다양한 문제가 발생할 수 있고,
# 이 때문에 super.x 와 같은 접근이 가능하지 못하게 설계 되었다 하면.....

# 그런데 여기서 하나 의문이 생긴다.....
# 다중상속일 경우를 위해 상속받은 [부모클래스명].[속성] 으로 접근이 가능하다고 했을때
# super() 는 도대체 어떤 클래스를 생성 할까???????????!!!!!!!!!!!!!!!!!!!

# super()는 다중 상속을 받아 생성되는 별도의 하나의 객체를 생성하는 하나의 클래스이며
# super == parent 가 성립하지 않는다
# 상속문에 나열한 순서로 생성되며
# 부모객체간 overriding 은 일어나지 않는 것인지 역순으로 overriding 되는 것인지.... 가장 앞의 부모를 우선한다.
# 만약 child2는 model2, model 순서로 상속받는다 하면
# model2.what = 2
# model.what = 1
# 이므로 model2 의 what 이 생성되어 메모리에 올라가고, model.what 은 버려진다.?!?!?!?!?
# 때문에 model2.what = super().what 이 되는 것이다.

# 이런 일련의 과정들(상속의 우선순위, 생성순서, 중복 속성의 선택 등)은
# super 라는 별도의 클래스에 의해 정의되며, super() 생성자는 이러한 객체를 만들고 해당 객체를 return 하는 것!

class child2(model2, model):
    __tablename__ = "asd"
    def get_super_attr(self):
        print(super().what, type(super()))
        print(model2.what == super().what)

ch2 = child2()
ch2.get_super_attr()
print(ch2.__table__)

# 아래서 볼수 있듯이, 생성하지 않고는 호출 불가...당연하지만....
# static 선언에 대해서는 좀더 알아볼 것!
# 특히 정적 변수.....
# print(child2.get_super_attr())
#############################################################################################################

# 이상 다중 상속의 맛은 조금 보았고, inner 클래스의 생성 및 활용에 대해서도 알아보았다.
# inner 클래스는 어찌보면 단순하게 멤버로 다른 클래스형을 가지는 형태로 생각 할 수 있지만,
# 그 사용용도와, 객체가 생성되는 시점과 내부에서의 동작을 정의 해 주어야 하는 점에서 차이가 있을 듯 하다.
# 상속과 클래스를 자유자재로 다루는 능력은 객체 지향이건 함수 지향이건 무조건 능숙하게 다루도록 하자.
# 객체 & class 라는 개념을 안쓸 이유가 없는 듯

outer_data = (1,2,3,4,5,4,3,2,1)

class A:
    attr1 = "A.attr1"
    attr2 = "A.attr2"
    def __init__(self, outer_data):
        self.outerdata_result = list(outer_data)

class B:
    attr1 = "B.attr1"
    attr2 = "B.attr2"
    def __init__(self, outer_data):
        self.outerdata_result = set(outer_data)

# 생성자 상속과 상속 순서의 확인
class Ch1(A, B):
    def __str__(self):
        return str(self.outerdata_result)
class Ch2(B, A):
    def __str__(self):
        return str(self.outerdata_result)

ch = Ch1(outer_data=outer_data)
print(ch)
print(ch.attr1)

ch = Ch2(outer_data=outer_data)
print(ch)
print(ch.attr1)

# 만약 A의 멤버를 사용하고 싶고, B의 생성자을 사용하고 싶다면
outer_data = (1,2,3,4,5,4,3,2,1)

class A:
    attr1 = "A.attr1"
    attr2 = "A.attr2"
    def method_A(self):
        print("A")
    def __init__(self, outer_data):
        print("생성자 A 호출")
        self.outerdata_result = list(outer_data)

class B:
    attr1 = "B.attr1"
    attr2 = "B.attr2"
    def method_B(self):
        print("B")
    def __init__(self, outer_data):
        print("생성자 B 호출")
        self.outerdata_result = set(outer_data)
        
class Ch3(B, A):
    def __init__(self, outer_data):
        print("자식 생성자 호출")

        ###################################################################################
        # B.__init__(self, outer_data)
        A.__init__(self, outer_data)
        # super(__class__, self).__init__(outer_data)
        ###################################################################################

        print("자식 생성자 종료")

    def __str__(self):
        return str(self.outerdata_result)
print("############################################################################")
ch = Ch3(outer_data)
print(ch.attr1, ch.attr2, ch)
ch.method_A()
ch.method_B()

# 위 예제 코드는 상속의 순서와 super활용으로
# super().__init__ 메서드조차 상속의 순서인 B 의 그것으로 정의된 것을 알 수 있다.
# 각 부모객체는 __init__ 에서 outerdata_result 만을 정의 하므로....
# __init__ 이 호출된 클래스에 따라  outerdata_result, __str__ 만 변화한다.



# 다이아몬드 상속문제라는게 있다고는 하는데....
# 다중 상속의 경우 최상위 생성자가 두번 호출되는 경우가 발생하고, 이의 호출 순서에 따라
# 얘기치 못한 상황이 발생한다고는 하는데...
# 잘 정리된 문서로 다시 찾아봐야겠다....
# super 클래스와 MRO 등등...