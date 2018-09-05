import datetime

from bs4 import BeautifulSoup
import pandas as pd
import modules.collection.crawler as cw
from db_accessing import Music_VO, db
from modules.collection.urlMaker import UrlMaker

class Collector:
    def crawling_mnet_month_chart(url):
        # mnet monthly chart 로부터 음원 데이터를 긁어오는 과정...
        results = {"Music_ID" : [], "Title" : [], "Singer" : [], "Album" : []}
        RESULT_DIRECTORY = '__result__'
        MVO = Music_VO()

        html = cw.crawling(url=url)
        bs = BeautifulSoup(html, 'html.parser')

    #####################################################################################################################
        # VO 값 입력
        tag_music_list = bs.find('div', attrs={'class': 'MMLTable jQMMLTable'})
        tag_tbody = tag_music_list.find('tbody')
        tags_tr = tag_tbody.findAll('tr')
        with db.session.no_autoflush:
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            for tag_tr in tags_tr:
                # item_title 태그내 정보들...
                item_title_tag_td = tag_tr.find('td', attrs={'class': 'MMLItemTitle'})
                # 음원의 고유 아이디
                MVO.Music_ID = tag_tr.find('td', attrs={'class': 'MMLItemCheck'}).find('input')["value"]

                MVO.Title = item_title_tag_td.find('a', attrs={'class': 'MMLI_Song'}).get_text()
                MVO.Singer = item_title_tag_td.find('a', attrs={'class': 'MMLIInfo_Artist'})
                if MVO.Singer != None:
                    MVO.Singer = MVO.Singer.get_text()
                MVO.Album = item_title_tag_td.find('a', attrs={'class': 'MMLIInfo_Album'})
                if MVO.Album != None:
                    MVO.Album = MVO.Album.get_text()

                print(MVO.Album)

                db.session.merge(MVO)

                ####################################################################################################################
                results["Music_ID"].append(MVO.Music_ID)
                results["Title"].append(MVO.Title)
                results["Singer"].append(MVO.Singer)
                results["Album"].append(MVO.Album)

            db.session.commit()

        table = pd.DataFrame(results, columns=['Music_ID', 'Title', 'Singer', 'Album'])

        table.to_json('{0}/mnet_weeks_100.json'.format(RESULT_DIRECTORY))

        table.to_csv('{0}/mnet_weeks_100.csv'.format(RESULT_DIRECTORY))


    # db.session.add(testVO)
    # 주 키 중복 시 IntegrityError 발생
    # 하지만 DB에서 발생한 에러를 위의 이름으로 돌려주고 해당 쿼리에 대한 롤백을 수행해야 함.
    # 무슨 이유에서인지 포문을 이탈하고 현재상태를 커밋 할 수 없게 됨....
    # 때문에 위의 merge 를 사용....
    #
    # 아래는 동작
    # try:
    #     db.session.add(testVO)
    #     db.session.commit()
    # except exc.IntegrityError as e:
    #     db.session().rollback()

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

    def __init__(self, start_date = datetime.date(2009, 1, 1), end_date = datetime.datetime.now().date()):
        self.start_date = start_date
        self.end_date = end_date