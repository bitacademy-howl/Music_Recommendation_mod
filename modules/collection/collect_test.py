import datetime

from bs4 import BeautifulSoup
import modules.collection.crawler as cw
from db_accessing import Music_VO, db, Album_VO
from modules.collection.urlMaker import UrlMaker

class Collector:
    def crawling_mnet_month_chart(url):
        # crawling_from_chart
        # mnet monthly chart 로부터 음원 데이터를 긁어오는 과정...
        # VO 객체들
        musicVO = Music_VO()
        albumVO = Album_VO()

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

            musicVO.Album_ID = item_title_tag_td.find('div', attrs={'class': 'MMLITitle_Album'}).find('a')

            if musicVO.Album_ID != None:
                music_node = musicVO.Album_ID["href"].strip(" ")

                musicVO.Album_ID = int(music_node.rsplit('/', 1)[1])
                albumVO.Album_ID = int(music_node.rsplit('/', 1)[1])

                db.session.merge(albumVO)
                db.session.commit()
                db.session.merge(musicVO)
                db.session.commit()

            # db.session.commit()

    def crawling_track(node):
        um = UrlMaker()
        url = um.direct_node_connect(node)
        html = cw.crawling(url=url)
        bs = BeautifulSoup(html, 'html.parser')
        print(bs)

    # 메인에서 호출할 함수들.....
    def Collecting(self):
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

    def __init__(self, start_date=datetime.date(2018, 8, 1), end_date=datetime.datetime.now().date()):
    # def __init__(self, start_date = datetime.date(2009, 1, 1), end_date = datetime.datetime.now().date()):

        self.start_date = start_date
        self.end_date = end_date
