from datetime import datetime as dt
from itertools import count
from bs4 import BeautifulSoup
import pandas as pd

import modules.collection.crawler as cw
from VO import db, test_VO

def inner_crawing():
    pass

def crawling_test():
    # CSV 파일입출력 하기 위한...
    results = {"Music_ID" : [], "Title" : [], "Singer" : [], "Album" : []}
    RESULT_DIRECTORY = '__result__'

    year = 2017
    testVO = test_VO()

    for month in range(1, 2, 1):
        page = "%s0%s" % (year, month)
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
            db.session.merge(testVO)

####################################################################################################################
            results["Music_ID"].append(testVO.Music_ID)
            results["Title"].append(testVO.Title)
            results["Singer"].append(testVO.Singer)
            results["Album"].append(testVO.Album)

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
        db.session.commit()


    # 데이터 프레임을 이용하여 json 형식, csv 형식으로 저장
    table = pd.DataFrame(results, columns=['Music_ID', 'Title', 'Singer', 'Album'])

    table.to_json('{0}/mnet_weeks_100.json'.format(RESULT_DIRECTORY))
    table.to_csv('{0}/mnet_weeks_100.csv'.format(RESULT_DIRECTORY))