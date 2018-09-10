import sys
from bs4 import BeautifulSoup

from db_accessing import db_session
from db_accessing.VO import Music_VO, Album_VO, Artist_VO
from modules.collection import crawler as cw

artistVO = Artist_VO()
artistVO.Artist_ID = 146749;
db_session.merge(artistVO)
db_session.commit()

for id in range(33801010, 33801015):

    musicVO = Music_VO()
    albumVO = Album_VO()

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