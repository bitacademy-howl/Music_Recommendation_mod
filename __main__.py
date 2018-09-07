# 데이터 시작은 2009년 1월 1일부터로 한다.
# 이유 : 2007, 2008년 연간 차트 존재, but 주간 및 일간차트 존재하지 않음
from db_accessing import *
from db_accessing.VO import Music_VO

if __name__ == '__main__':
    from modules.collection.collect import Collector
    col = Collector()
    col.set_start_date(2018, 8, 1)
    col.collecting_chart()

    # (join 미 수행 시) select 쿼리 각각의 result 는 VO객체의 리스트로 전달됨
    # result = Music_VO.query.limit(4).offset(4051).all()
    #
    # print(len(result), print(result))
    #
    # res = Music_VO.query.count()
    # print(res)
    # print(Music_VO.query)







