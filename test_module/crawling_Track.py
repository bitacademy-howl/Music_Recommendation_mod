# 값을 입력할 VO 객체 생성
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from db_accessing import db_session
from modules.collection import crawler as cw
from db_accessing.VO import Music_VO
from modules.collection.urlMaker import UrlMaker, URL_Node

def crawling_track(um):

    musicVO = Music_VO()
    musicVO.Music_ID = um.END_POINT
    musicVO.Music_Node = '/'.join([um.NODE, str(um.END_POINT)])

    html = cw.crawling(url=um.URL)
    bs = BeautifulSoup(html, 'html.parser')
    tag_music_info = bs.find('div', attrs={'class': 'music_info_view'})

    if tag_music_info is not None:
        # 곡 소개 테이블
        summary = tag_music_info.find('div', attrs={'class': 'music_info_cont'})
        album_tag = summary.find('table').find('a')

        if album_tag is not None:
            musicVO.Album_Node = album_tag['href'].strip(" ")
            musicVO.Album_ID = int(musicVO.Album_Node.rsplit('/', 1)[1])

        # attrs = summary.find('li', attrs={'class': 'left_con'}).findAll('p', attrs={'class': 'right'})
        musicVO.Music_Title = tag_music_info.find('li', attrs={'class' : 'top_left'})
        if musicVO.Music_Title is not None:
            musicVO.Music_Title = musicVO.Music_Title.find('p').get_text().strip()

        left_attrs = summary.find('li', attrs={'class': 'left_con'}).findAll('p', attrs='left')
        right_attrs = summary.find('li', attrs={'class': 'left_con'}).findAll('p', attrs='right')

        for i in range(0, len(left_attrs)):
            if left_attrs[i].get_text().strip() == '음악장르':
                musicVO.Genre = right_attrs[i].get_text().strip()



        line_info = tag_music_info.findAll('div', attrs={'class': 'line_info'})
        lyric = line_info[0].find('li', attrs={'id': 'lyricsText'})
        if len(line_info) > 1:
            staffs = line_info[1].findAll('ul', attrs={'class': 'con2'})
        else:
            staffs = None

        if lyric is not None:
            musicVO.Lyrics = lyric.get_text().replace('\n', '').replace('\t', '').replace('<br/>', '\n').strip()

        if staffs is not None:
            for staff in staffs:
                lyricists = ''
                if staff.find('li', attrs={'class': 'title'}).get_text().strip() == '작사':
                    for lyricist in staff.findAll('a'):
                        lyricists = ','.join([lyricists, lyricist['href'].strip().rsplit('/', 1)[1]])
                    musicVO.Lyricist_ID = lyricists.split(',', 1)[1]

                if staff.find('li', attrs={'class': 'title'}).get_text().strip() == '작곡':
                    comporsers = ''
                    for comporser in staff.findAll('a'):
                        comporsers = ','.join([comporsers, comporser['href'].strip().rsplit('/', 1)[1]])
                    musicVO.Composer_ID = comporsers.split(',', 1)[1]

        print(musicVO)
        db_session.merge(musicVO)

def collecting_track(start_index = 1):
    um = UrlMaker()

    for id in range(start_index, 10000000):
        um.set_param(node=URL_Node.TRACK, end_point=id)
        crawling_track(um)
        # try:
        #     crawling_track(um)
        # except Exception as e:
        #     print(e)
        #     print('exception [{0}] \nID : {1}'.format(datetime.now(), id))
        #     sleep(300)
        #     print('sleep 해제')
        #     return collecting_track(id)

        sleep(0.5)

        if id%5 == 0:
            db_session.commit()

collecting_track()