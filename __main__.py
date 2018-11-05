# 데이터 시작은 2009년 1월 1일부터로 한다.
# 이유 : 2007, 2008년 연간 차트 존재, but 주간 및 일간차트 존재하지 않음

import threading
from time import sleep
from sqlalchemy import desc
from db_accessing.VO import Music_VO, Album_VO, Artist_VO

if __name__ == '__main__':

    ar_start_condition = Artist_VO.query.filter(Artist_VO.Artist_ID < 10000000).order_by(desc("Artist_ID")).first().Artist_ID
    al_start_condition = Album_VO.query.order_by(desc("Album_ID")).first().Album_ID
    ti_start_condition = Music_VO.query.order_by(desc("Music_ID")).first().Music_ID


    # 초기 쓰레드
    from modules.collection import collecting_track, collecting_album, collecting_artist
    t1 = threading.Thread(target=collecting_artist, args=[Artist_VO.query.filter(Artist_VO.Artist_ID<10000000).order_by(desc("Artist_ID")).first().Artist_ID])
    print(Album_VO.query.order_by(desc("Album_ID")).first().Album_ID, type(Album_VO.query.order_by(desc("Album_ID")).first().Album_ID))
    t2 = threading.Thread(target=collecting_album, args=[Album_VO.query.order_by(desc("Album_ID")).first().Album_ID])
    print(Music_VO.query.order_by(desc("Music_ID")).first().Music_ID)
    t3 = threading.Thread(target=collecting_track, args=[Music_VO.query.order_by(desc("Music_ID")).first().Music_ID])
    print(Music_VO.query.order_by(desc("Music_ID")).first().Music_ID)

    # t1 = threading.Thread(target=collecting_artist, args=[627853])
    # t2 = threading.Thread(target=collecting_album, args=[664139])
    # t3 = threading.Thread(target=collecting_track, args=[770876])

    ar_start_condition = Artist_VO.query.filter(Artist_VO.Artist_ID < 10000000).order_by(
        desc("Artist_ID")).first().Artist_ID
    al_start_condition = Album_VO.query.order_by(desc("Album_ID")).first().Album_ID
    ti_start_condition = Music_VO.query.order_by(desc("Music_ID")).first().Music_ID

    # 2018 - 10 - 16
    # 15: 53:45.055467: Success
    # for request[http: // www.mnet.com / artist / 627853]
    # < Artist_table(Artist_ID: 627853, Artist_Name: DJ
    # DKHT, Gender: 남성, Group: False, Artist_Node: artist / 627853) >

    # 2018 - 10 - 16
    # 15: 53:45.169595: Success
    # for request[http: // www.mnet.com / album / 664139]

    # 2018 - 10 - 16
    # 15: 53:45.107076: Success
    # for request[http: // www.mnet.com / track / 770876]

    #
    while(True):
        if not t1.is_alive():
            print("if문 1")
            t1 = threading.Thread(target=collecting_artist, args=[ar_start_condition])
            t1.start()
            
        if not t2.is_alive():
            print("if문 2")
            t2 = threading.Thread(target=collecting_album, args=[al_start_condition])
            t2.start()
        if not t3.is_alive():
            print("if문 3")
            t3 = threading.Thread(target=collecting_track, args=[ti_start_condition])
            t3.start()

        sleep(2)

# 2018-10-11 12:33:21.312067 : Success for request [http://www.mnet.com/track/694713]
# 저장된 가사 :  None
# 2018-10-11 12:33:21.608897 : Success for request [http://www.mnet.com/album/592839]
# 2018-10-11 12:33:21.749461 : Success for request [http://www.mnet.com/artist/575959]