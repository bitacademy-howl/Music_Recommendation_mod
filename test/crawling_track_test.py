import sys
from bs4 import BeautifulSoup

from db_accessing import db_session
from db_accessing.VO import Music_VO, Album_VO, Artist_VO
from modules.collection import crawler as cw

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
                right_span_a_tag = right_span.find('a')
                if right_span_a_tag is not None:
                    albumVO.Singer_ID = int(right_span_a_tag['href'].strip().rsplit('/', 1)[1])
                else:
                    albumVO.Singer_ID = Artist_VO.query.filter_by(Artist_Name='Various Artists').first().Artist_ID
                    # albumVO.Singer_ID = 10000000
            if left_span == '발매일':
                ymd = [1,1,1]
                ymd_data = list(map(lambda x: int(x), right_span.get_text().split('.')))
                for i in range(len(ymd_data)):
                    if i == 0 and 0 < ymd_data[i]:
                        ymd[i] = ymd_data[i]
                    elif i == 1 and 0 < ymd_data[i] < 13:
                        ymd[i] = ymd_data[i]
                    elif i == 2 and 0 < ymd_data[i] < 32:
                        ymd[i] = ymd_data[i]
                albumVO.Release_Date = datetime(ymd[0], ymd[1], ymd[2])

            if left_span == '기획사' or left_span == '레이블':
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
    # for id in range(1, 10000000):
    for id in range(10740, 10000000):
        um.set_param(node=URL_Node.ALBUM, end_point=id)
        try:
            crawling_album(um)
        except Exception as e:
            sleep(60*1)
            print(e)
            crawling_album(um)
            # id -= 1     # 이건 어차피 안될듯... range 에서 id 를 가져오는 for 의 특성
            continue

        # sleep(0.5)

        if id%5 == 0:
            db_session.commit()

collecting_album()


for id in range(33801010, 33801015):

    musicVO = Music_VO()

    musicVO.Music_ID = id

    # bs from html response....
    musicVO.Music_Node = '/track/{0}'.format(id)
    html = cw.crawling(url="http://www.mnet.com%s" % musicVO.Music_Node)

    bs = BeautifulSoup(html, 'html.parser')
    tag_music_info = bs.find('div', attrs={'class': 'music_info_view'})

    if tag_music_info is not None:
        # 곡 소개 테이블
        summary = tag_music_info.find('div', attrs={'class': 'music_info_cont'})
        album_tag = summary.find('table').find('a')

        if album_tag is not None:
            albumVO.Album_Node = album_tag['href'].strip(" ")
            musicVO.Album_ID = int(albumVO.Album_Node.rsplit('/', 1)[1])
            albumVO.Album_ID = int(albumVO.Album_Node.rsplit('/', 1)[1])

        artist_tag = summary.find('span', attrs={'class': 'artist_txt'}).find('a')

        if artist_tag != None:
            albumVO.Singer_ID = int(artist_tag['href'].strip(" ").rsplit('/', 1)[1])

        # attrs = summary.find('li', attrs={'class': 'left_con'}).findAll('p', attrs={'class': 'right'})
        musicVO.Music_Title = tag_music_info.find('li', attrs={'class' : 'top_left'}).get_text().strip()
        left_attrs = summary.find('li', attrs={'class': 'left_con'}).findAll('p', attrs='left')
        right_attrs = summary.find('li', attrs={'class': 'left_con'}).findAll('p', attrs='right')
        for i in range(0, len(left_attrs)):
            if left_attrs[i].get_text().strip() == '발매일':
                albumVO.Release_Date = right_attrs[i].get_text()
            if left_attrs[i].get_text().strip() == '음악장르':
                musicVO.Genre = right_attrs[i].get_text().strip()
            if left_attrs[i].get_text().strip() == '작사':
                for lyricist in right_attrs[i].findAll('a', attrs='href'):
                    Music_VO.Lyricist.append(Artist_VO.query.filter_by(Artist_ID = int(lyricist.strip().rsplit('/', 1))))
            if left_attrs[i].get_text().strip() == '작곡':
                for comporser in right_attrs[i].findAll('a', attrs='href'):
                    Music_VO.Composer.append(Artist_VO.query.filter_by(Artist_ID = int(comporser.strip().rsplit('/', 1))))

        db_session.merge(albumVO)
        db_session.commit()

        db_session.merge(musicVO)

db_session.commit()

print(musicVO, albumVO)