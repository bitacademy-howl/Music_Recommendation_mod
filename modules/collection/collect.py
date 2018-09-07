import datetime

from bs4 import BeautifulSoup
import modules.collection.crawler as cw
from db_accessing import *
from db_accessing.VO import Music_VO, Artist_VO, Album_VO
from modules.collection.urlMaker import UrlMaker

class Collector:
    def crawling_mnet_month_chart(url):
        # crawling_from_chart
        # mnet monthly chart 로부터 음원 데이터를 긁어오는 과정...
        # VO 객체들
        artistVO = Artist_VO()
        albumVO = Album_VO()
        musicVO = Music_VO()

        html = cw.crawling(url=url)
        bs = BeautifulSoup(html, 'html.parser')

    #####################################################################################################################
        # VO 값 입력
        tag_music_list = bs.find('div', attrs={'class': 'MMLTable jQMMLTable'})
        tag_tbody = tag_music_list.find('tbody')
        tags_tr = tag_tbody.findAll('tr')

        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        for tag_tr in tags_tr:
            # item_title 태그내 정보들...
            item_title_tag_td = tag_tr.find('td', attrs={'class': 'MMLItemTitle'})

            # 8개 해야된다......
            # 음원의 고유 아이디
            musicVO.Music_ID = tag_tr.find('td', attrs={'class': 'MMLItemCheck'}).find('input')["value"]

            musicVO.Music_Title = item_title_tag_td.find('a', attrs={'class': 'MMLI_Song'}).get_text()

            album_tag = item_title_tag_td.find('a', attrs={'class': 'MMLIInfo_Album'})
            artist_tag = item_title_tag_td.find('a', attrs={'class': 'MMLIInfo_Artist'})

            print(album_tag)
            print(artist_tag)

            if album_tag != None:
                albumVO.Album_Title = album_tag.get_text()
                albumVO.Album_Node = album_tag["href"].strip(" ")
                albumVO.Album_ID = int(albumVO.Album_Node.rsplit('/', 1)[1])
                musicVO.Album_ID = albumVO.Album_ID

            if artist_tag != None:
                artistVO.Artist_Name = artist_tag.get_text()

                # 객체 및 테이블에 노드 추가 할 것!
                artistVO.Artist_Node = artist_tag["href"].strip(" ")

                artistVO.Artist_ID = int(artistVO.Artist_Node.rsplit('/', 1)[1])
                albumVO.Singer_ID = artistVO.Artist_ID

            # #######commit 계속 안하고 한방에 못하는지 알아보고, ORM 객체 내 객체 포함...으로 알아볼 것!!!
            # 양방향 머시기 하는듯...
            db_session.merge(artistVO)
            db_session.commit()
            db_session.merge(albumVO)
            db_session.commit()
            db_session.merge(musicVO)
            db_session.commit()

    def crawling_track(url):
        # 값을 입력할 VO 객체 생성
        musicVO = Music_VO()
        albumVO = Album_VO()
        artistVO = Artist_VO()

        # bs from html response....
        html = cw.crawling(url=url)
        bs = BeautifulSoup(html, 'html.parser')
        # 곡 소개 테이블
        summary = bs.find('div', attrs={'class': 'music_info_cont'})
        album_tag = summary.find('tbody').find('a')

        if album_tag is not None:
            albumVO.Album_Node = album_tag['href'].strip(" ")
            albumVO.Album_ID = albumVO.Album_Node.rsplit('/', 1)[1]
            musicVO.Album_ID = albumVO.Album_ID

        artist_tag = bs.find('span', attrs={'class': 'artist_txt'}).find('a')

        if artist_tag != None:
            artistVO.Artist_Node = artist_tag['href'].strip(" ")
            artistVO.Artist_ID = artistVO.Artist_Node.rsplit('/', 1)[1]
            artistVO.Artist_Name = artist_tag.get_text()
            albumVO.Singer_ID = artistVO.Artist_ID

        tag_music_info = bs.find('div', attrs={'class': 'music_info_view'})

        summary = tag_music_info.find('li', attrs={'class': 'left_con'})
        tags_tr = summary.findAll('p', attrs={'class': 'right'})


    # 메인에서 호출할 함수들.....
    def collecting_track(self, node):
        um = UrlMaker()
        row_num_table = Music_VO.qurey.count()

        for offs in range(0, row_num_table, 10):
            result = Music_VO.query.limit(10).offset(offs).all()
            for i in result:
                self.crawling_track(um.direct_node_connect(i.Music_Node))


    def collecting_chart(self):
        um = UrlMaker()
        for year in range(self.start_date.year, self.end_date.year+1):
            for month in range(self.start_date.month, self.end_date.month+1):
                try:
                    um.setDate(datetime.date(year, month, day=1))
                    um.url_maker_DATE_based()

                    for page_number in range(1, 3):
                        url = "".join([um.url_maker_DATE_based(), '?pNum=%d' % page_number])
                        print(url)
                        Collector.crawling_mnet_month_chart(url)

                except ValueError:
                    break

    # def __init__(self, start_date=datetime.date(2009, 1, 1), end_date=datetime.datetime.now().date()):
    # # def __init__(self, start_date = datetime.date(2009, 1, 1), end_date = datetime.datetime.now().date()):
    #     self.start_date = start_date
    #     self.end_date = end_date

    def __init__(self):
        self.set_start_date()
        self.end_date = datetime.datetime.now().date()

    def set_start_date(self, year = 2009, month = 8, day = 1):
        self.start_date = datetime.date(2009, 8, 1)

    def set_end_date(self, year, month, day):
        self.end_date = datetime.date(year, month, day)