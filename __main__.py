# 데이터 시작은 2009년 1월 1일부터로 한다.
# 이유 : 2007, 2008년 연간 차트 존재, but 주간 및 일간차트 존재하지 않음

import threading
from time import sleep
from sqlalchemy import desc
from db_accessing.VO import Music_VO, Album_VO, Artist_VO

if __name__ == '__main__':

    from modules.collection import collecting_track, collecting_album, collecting_artist
    t1 = threading.Thread(target=collecting_artist, args=[Artist_VO.query.filter(Artist_VO.Artist_ID<10000000).order_by(desc("Artist_ID")).first().Artist_ID])
    t2 = threading.Thread(target=collecting_album, args=[Album_VO.query.order_by(desc("Album_ID")).first().Album_ID])
    t3 = threading.Thread(target=collecting_track, args=[Music_VO.query.order_by(desc("Music_ID")).first().Music_ID])

    while(True):

        if not t1.is_alive():
            t1.start()
        if not t2.is_alive():
            t2.start()
        if not t3.is_alive():
            t3.start()

        sleep(1800)

