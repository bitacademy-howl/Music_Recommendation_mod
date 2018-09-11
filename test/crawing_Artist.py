import time

from bs4 import BeautifulSoup
from db_accessing import db_session
from db_accessing.VO import Album_VO, Music_VO, Artist_VO
from modules.collection import crawler

# for id in range(1, 3000000, 1):
for id in range(95966, 10000000, 1):
# for id in range(1, 30, 1):

    artistVO = Artist_VO()
    artistVO.Artist_ID = id
    artistVO.Artist_Node = '/artist/{0}'.format(id)
    artistVO.Group = False

    url = ''.join(['http://www.mnet.com', artistVO.Artist_Node])
    html = crawler.crawling(url)
    bs = BeautifulSoup(html, 'html.parser')
    tag_artist_info = bs.find('div', attrs={'class': 'artist_info'})

    if tag_artist_info is not None:
        singer = tag_artist_info.find('a', attrs={'class': 'song_name'})
        if singer is not None:
            artistVO.Artist_Name = singer.get_text()
        else:
            artistVO.Artist_Name = tag_artist_info.find('li', attrs={'class' : 'top_left'}).find('p').get_text().strip()
            print("############# strip 결과 #############\n", artistVO.Artist_Name, "\n############# strip 결과 #############\n")

        a= tag_artist_info.find('div', attrs = {'class' : 'a_info_cont'})

        tags = tag_artist_info.findAll('span', attrs={'class' : 'right'})
        for tag in tags:
            if tag is not None:
                text_list = tag.get_text().strip().replace(' ', '').replace('\r', '').replace('\n', '').replace('\t', '').replace('\xa0', '').split('|')
                print(text_list)
                for text in text_list:
                    if text == '남성' or text == '여성' or text == '혼성':
                        artistVO.Gender = text
                    if text == '그룹':
                        artistVO.Group = True
        db_session.merge(artistVO)
        db_session.commit()

    time.sleep(0.5) # sleep 안주면 200 번째 request 이후 차단됨...