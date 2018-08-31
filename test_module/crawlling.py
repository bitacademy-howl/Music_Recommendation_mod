from datetime import datetime as dt
from itertools import count
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import exc

import modules.collection.crawler as cw
from VO import db, test_VO


def crawling_test():
    results = []
    RESULT_DIRECTORY = '__result__'

    year = 2017
    testVO = test_VO()

    for month in range(1, 2, 1):
        page = "%s%s" % (year, month)
        url = 'http://www.mnet.com/chart/TOP100/{0}'.format(page)
        html = cw.crawling(url=url)
        bs = BeautifulSoup(html, 'html.parser')

        # VO 값 입력
        tag_music_list = bs.find('div', attrs={'class': 'MMLTable jQMMLTable'})
        tag_tbody = tag_music_list.find('tbody')
        # tag_tbody = bs.find('tbody')
        tags_tr = tag_tbody.findAll('tr')

        for tag_tr in tags_tr:
            # item_title 태그내 정보들...
            item_title_tag_td = tag_tr.find('td', attrs={'class': 'MMLItemTitle'})

            testVO.Title = item_title_tag_td.find('a', attrs={'class': 'MMLI_Song'}).get_text()
            testVO.Singer = item_title_tag_td.find('a', attrs={'class': 'MMLIInfo_Artist'}).get_text()
            testVO.Album = item_title_tag_td.find('a', attrs={'class': 'MMLIInfo_Album'}).get_text()

            # 음원의 고유 아이디
            testVO.Music_ID = tag_tr.find('td', attrs={'class': 'MMLItemCheck'}).find('input')["value"]

            # 제대로 동작 X SQL 쿼리문 中 IGNORE 기능을 설정하는 부분을 찾아야함
            try:
                db.session.add(testVO)
                db.session.commit()
            except exc.IntegrityError as e:
                db.session().rollback()
                continue

    title = list(set(results))

    # store
    # table = pd.DataFrame(a, columns=['title', '', '', ''])
    table = pd.DataFrame(title, columns=['title'])
    table.to_csv('{0}/mnet_weeks_100.csv'.format(RESULT_DIRECTORY))