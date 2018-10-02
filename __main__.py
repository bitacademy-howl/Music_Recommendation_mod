# 데이터 시작은 2009년 1월 1일부터로 한다.
# 이유 : 2007, 2008년 연간 차트 존재, but 주간 및 일간차트 존재하지 않음

import threading

if __name__ == '__main__':
    # from modules.collection.collect import start_crawling
    # start_crawling(start_index_of_artist=, start_index_of_album=, start_index_of_track=)

    from modules.collection import collecting_track, collecting_album, collecting_artist

    t1 = threading.Thread(target=collecting_artist, args=[495375])
    t2 = threading.Thread(target=collecting_album, args=[510602])
    t3 = threading.Thread(target=collecting_track, args=[544105])

    t1.start()
    t2.start()
    t3.start()