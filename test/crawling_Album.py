from datetime import datetime
from time import sleep

from bs4 import BeautifulSoup, NavigableString

from db_accessing import db_session
from db_accessing.VO import Album_VO
from modules.collection import crawler as cw
from modules.collection.urlMaker import UrlMaker, URL_Node

def crawling_album(um = UrlMaker()):
    # UrlMaker 객체를 매개변수로 넘겨받아서 1페이지를 크롤링
    albumVO = Album_VO()
    albumVO.Album_ID = um.END_POINT
    albumVO.Album_Node = '/'.join([um.NODE, str(um.END_POINT)])

    # bs from html response....
    html = cw.crawling(url=um.URL)
    bs = BeautifulSoup(html, 'html.parser')
    tag_Album_info = bs.find('div', attrs={'class': 'album_info'})

    if tag_Album_info is not None:
        # 아래는 태그자체가 앨범타이틀로 들어갈 수 있으니 주의할 것! 확인 요망
        albumVO.Album_Title = tag_Album_info.find('li', attrs={'class': 'top_left'})
        if albumVO.Album_Title is not None:

            albumVO.Album_Title = albumVO.Album_Title.find('p').get_text().strip()

        album_info = tag_Album_info.find('div', {'class' : 'a_info_cont'})

        summary = album_info.find('dl').find('dd').findAll('p')

        for tag in summary:
            left_span = tag.find('span', attrs={'class', 'left'}).get_text()
            right_span = tag.find('span', attrs={'class', 'right'})

            if left_span == '아티스트':
                left_span_a_tag = right_span.find('a')
                if left_span_a_tag is not None:
                    albumVO.Singer_ID = int(left_span_a_tag['href'].strip().rsplit('/', 1)[1])
            if left_span == '발매일':
                text = right_span.get_text()
                comparer = text.split('.')
                try:
                    if len(comparer) == 3:
                        albumVO.Release_Date = datetime.strptime(text, '%Y.%m.%d')
                    elif len(comparer) == 1:
                        albumVO.Release_Date = datetime.strptime(text, '%Y')
                except ValueError:
                    date = right_span.get_text().rsplit('.', 1)[0]
                    albumVO.Release_Date = datetime.strptime(date, '%Y.%m')
            if left_span == '기획사':
                albumVO.Agency = right_span.get_text().strip()
            if left_span == '유통사':
                albumVO.Distributor = right_span.get_text().strip()

        descriptions = album_info.find('div', attrs={'class', 'text_slider'})

        if descriptions is not None:
            descriptions = descriptions.findAll('p')
            if len(descriptions) == 2:
                desc = str(descriptions[1])
            else:
                desc = descriptions.get_text().replace('\n', '').replace('\t', '')

            desc = desc.replace('<p class="txt">', '').replace('<br/>', '\n').replace('</p>', '').strip()
            albumVO.Description = desc

        db_session.merge(albumVO)

def collecting_album():
    # albums = [3188608, 1]
    um = UrlMaker()
    album_list = []
    for id in range(200, 10000000):
        um.set_param(node=URL_Node.ALBUM, end_point=id)
        # crawling_album(um)
        # print(um)
        crawling_album(um)
        sleep(0.5)

        if id%100 == 0:
            db_session.commit()

collecting_album()