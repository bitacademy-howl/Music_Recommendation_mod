# 데이터 시작은 2009년 1월 1일부터로 한다.
# 이유 : 2007, 2008년 연간 차트 존재, but 주간 및 일간차트 존재하지 않음

from modules.collection.collect import Collector

if __name__ == '__main__':
    col = Collector()
    col.Collecting()

    # print(Music_VO.query.filter_by(Singer="김건모").all())
    # print(db.session.query(Music_VO).filter(Music_VO.Singer.like("김건모%")).all())