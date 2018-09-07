from db_accessing import db_session
from db_accessing.VO import Music_VO

# ############################################################################################################
# # 컬럼이 일치하는 행
# # SELECT * from Music_VO.__table__ where Singer = "김건모"
# print(Music_VO.query.filter_by(Singer="김건모").all())
# ############################################################################################################
#
# ############################################################################################################
# # 아래에서 a : sql 구문
# #          b : sql 결과
#
# a = Music_VO.query.filter_by(Singer="김건모")
# print(a)
# b = a.all()
# print(b)
# ############################################################################################################

############################################################################################################
# like 문의 활용
print(Music_VO.query.filter(Music_VO.Music_Title.like("%love%")).all())
############################################################################################################

############################################################################################################
# count 활용
# SQL : SELECT COUNT(*) FROM music
print(Music_VO.query.count())
############################################################################################################

############################################################################################################
# ex : OFFSET 과 LIMIT
# SQL 문 >>>>>>>>>
# >>>>> SELECT * FROM table LIMIT 1 OFFSET 20;
# LIMIT : 가져올 row 의 최대 갯수...
# OFFSET : 테이블에서 건너 뛸 행의 갯수
#          ==> 즉, 시작지점의 주소값이라 생각하면 된다....(0 부터 시작)
# 
# sqlalchemy 에서는 아래의 함수로 쿼리문 작성
#############################################################################################################
print(Music_VO.query.offset(0).limit(5).all())
print(Music_VO.query.offset(1).limit(2).all())
print(Music_VO.query.offset(3).limit(1).all())
############################################################################################################

############################################################################################################
# 여기서 다시 잠깐....!!!
# 대부분의 함수들은 쿼리문을 작성하는 데 사용되고, all() 등의 SELECT 구문을 실행하여 VO 객체를 반환하는 함수는 따로 있다.
a = Music_VO.query.filter(Music_VO.Music_Title.like('%love%')).offset(0).limit(5)
print(a)          # <<<<<<<<< 쿼리 작성
print(a.all())    # <<<<<<<<< 객체화 하여 결과 리스트 return

# print(db_session.query(Music_VO).filter(Music_VO.Music_Title.like("%love%")).all())
# print(db_session.query(Music_VO).filter(Music_VO.Music_Title.like("%love%")).offset(20).all())
############################################################################################################

############################################################################################################
# 세션이 가지고 있는 쿼리 구문을 사용할 수도 있고, db_session.query(Music_VO)
# VO 객체 내 쿼리를 사용할 수도 있다.....
# 함수는 약간씩 다른것 같음....확인바람
############################################################################################################

############################################################################################################
# 객체 Relation 구현 후 테스트....
BBOOM = Music_VO.query.filter_by(Music_Title="뿜뿜").all()[0]
x = BBOOM.Album.Singer.Artist_Name
print(x)
print(BBOOM)
############################################################################################################