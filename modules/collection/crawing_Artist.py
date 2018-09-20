from datetime import datetime
import time
from time import sleep

from bs4 import BeautifulSoup
from db_accessing import db_session
from db_accessing.VO import Artist_VO
from modules.collection import crawler

from modules.collection.urlMaker import UrlMaker, URL_Node

def crawling_Artist(um):

    artistVO = Artist_VO()
    artistVO.Artist_ID = um.END_POINT
    artistVO.Artist_Node = '/'.join([um.NODE, str(um.END_POINT)])
    artistVO.Group = False

    html = crawler.crawling(url=um.URL)
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
                # print(text_list)
                for text in text_list:
                    if text == '남성' or text == '여성' or text == '혼성':
                        artistVO.Gender = text
                    if text == '그룹':
                        artistVO.Group = True

        db_session.merge(artistVO)
        db_session.commit()

        print(artistVO)

def collecting_artist(start_index = 1):
    um = UrlMaker()

    for id in range(start_index, 10000000):
        um.set_param(node=URL_Node.ARTIST, end_point=id)
        try:
            crawling_Artist(um)
        except Exception as e:
            print(e)
            print('exception [{0}] \nID : {1}'.format(datetime.now(), id))
            sleep(300)
            print('sleep 해제')
            return crawling_Artist(id)

        sleep(0.25)