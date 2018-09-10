# 값을 입력할 VO 객체 생성
from bs4 import BeautifulSoup
from modules.collection import crawler as cw
from db_accessing.VO import Music_VO, Album_VO, Artist_VO


def crawling_track(url):
    for id in range(1, 10000000):
        musicVO = Music_VO()
        albumVO = Album_VO()
        artistVO = Artist_VO()

        # Music_ID 는 링크로부터 채워서 올것!
        # Music_VO.Music_ID =

        # bs from html response....
        html = cw.crawling(url=url)
        bs = BeautifulSoup(html, 'html.parser')
        tag_music_info = bs.find('div', attrs={'class': 'music_info_view'})
        # 곡 소개 테이블
        summary = tag_music_info.find('div', attrs={'class': 'music_info_cont'})
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

        attrs = summary.find('li', attrs={'class': 'left_con'}).findAll('p', attrs={'class' : 'right'})
        albumVO.Release_Date = attrs[0].get_text()
        # Music_VO.