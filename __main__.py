# 데이터 시작은 2009년 1월 1일부터로 한다.
# 이유 : 2007, 2008년 연간 차트 존재, but 주간 및 일간차트 존재하지 않음

if __name__ == '__main__':
    # from modules.collection.collect import start_crawling
    # start_crawling(start_index_of_artist=, start_index_of_album=, start_index_of_track=)

    from modules.collection import collecting_track, collecting_album, collecting_artist
    # collecting_artist()
    # collecting_album()
    collecting_track(444595)


