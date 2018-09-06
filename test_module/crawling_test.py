from bs4 import BeautifulSoup

import modules.collection.crawler as cw
from test_module.db_accessing import db


def crawling_test():

    html = cw.crawling(url=url)
    bs = BeautifulSoup(html, 'html.parser')

    tag_music_list = bs.find('div', attrs={'class': 'MMLTable jQMMLTable'})
    tag_tbody = tag_music_list.find('tbody')
    tags_tr = tag_tbody.findAll('tr')

    for tag_tr in tags_tr:
        # item_title 태그내 정보들...
        item_title_tag_td = tag_tr.find('td', attrs={'class': 'MMLItemTitle'})

        test_VO.Title = item_title_tag_td.find('a', attrs={'class': 'MMLI_Song'}).get_text()
        testVO.Singer = item_title_tag_td.find('a', attrs={'class': 'MMLIInfo_Artist'}).get_text()
        testVO.Album = item_title_tag_td.find('a', attrs={'class': 'MMLIInfo_Album'}).get_text()

        # 음원의 고유 아이디
        testVO.Music_ID = tag_tr.find('td', attrs={'class': 'MMLItemCheck'}).find('input')["value"]

        # 제대로 동작 X SQL 쿼리문 中 IGNORE 기능을 설정하는 부분을 찾아야함
        db.session.merge(testVO)

    db.session.commit()