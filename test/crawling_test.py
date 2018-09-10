from datetime import datetime

from bs4 import BeautifulSoup

from db_accessing.VO import Album_VO, Music_VO, Artist_VO
from modules.collection import crawler

url = 'http://www.mnet.com/track/33801010'

html = crawler.crawling(url)

bs = BeautifulSoup(html, 'html.parser')
tag_music_info = bs.find('div', attrs={'class': 'music_info_view'})

albumVO = Album_VO()
musicVO = Music_VO()
artistVO = Artist_VO()

# 곡 소개 테이블
summary = tag_music_info.find('div', attrs={'class': 'music_info_cont'})
album_tag = summary.find('table').find('a')

musicVO.Music_ID = 33801010

if album_tag is not None:
    albumVO.Album_Node = album_tag['href'].strip(" ")
    albumVO.Album_ID = int(albumVO.Album_Node.rsplit('/', 1)[1])
    musicVO.Album_ID = albumVO.Album_ID

artist_tag = bs.find('span', attrs={'class': 'artist_txt'}).find('a')

if artist_tag != None:
    artistVO.Artist_Node = artist_tag['href'].strip(" ")
    artistVO.Artist_ID = int(artistVO.Artist_Node.rsplit('/', 1)[1])
    artistVO.Artist_Name = artist_tag.get_text()
    albumVO.Singer_ID = artistVO.Artist_ID

#####################################################################################

summary = tag_music_info.find('div', attrs={'class': 'music_info_cont'})
attrs = summary.find('li', attrs={'class': 'left_con'}).findAll('p', attrs={'class' : 'right'})
albumVO.Release_Date = datetime.strptime(attrs[0].get_text(), '%Y.%m.%d')
musicVO.Genre = attrs[1].get_text().strip(" ")

Lyricists = attrs[2].findAll('a', attrs='href')
for Lyricist in Lyricists:
    musicVO.Lyricist_ID.append(int(Lyricist.strip(" ").rsplit('/', 1)[1]))

Composers = attrs[3].findAll('a', attrs='href')
for Composer in Composers:
    musicVO.Composer_ID.append(int(Composer.strip(" ").rsplit('/', 1)[1]))

# print(albumVO.Release_Date, type(albumVO.Release_Date))

print(albumVO)
print(artistVO)
print(musicVO)

print("################################################################################################")
print(musicVO.Composer)
if musicVO.Composer_ID is not None:
    for i in musicVO.Composer_ID:
        print("composers : ", i)
