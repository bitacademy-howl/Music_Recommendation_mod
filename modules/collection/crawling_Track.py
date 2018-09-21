# 값을 입력할 VO 객체 생성
from builtins import WindowsError
from datetime import datetime
from time import sleep
import sys
from bs4 import BeautifulSoup
from sqlalchemy.exc import InternalError

from db_accessing import db_session
from modules.collection import crawler as cw
from db_accessing.VO import Music_VO
from modules.collection.urlMaker import UrlMaker, URL_Node
import os

def crawling_track(um):

    musicVO = Music_VO()
    musicVO.Music_ID = um.END_POINT
    musicVO.Music_Node = '/'.join([um.NODE, str(um.END_POINT)])

    html = cw.crawling(url=um.URL)
    bs = BeautifulSoup(html, 'html.parser')

    tag_music_info = bs.find('div', attrs={'class': 'music_info_view'})

    # 곡 정보가 존재하지 않는 페이지(없는 곡입니다) ....가 아닌 경우에만 수행 경우......
    if tag_music_info is not None:
        # 곡 소개 테이블
        summary = tag_music_info.find('div', attrs={'class': 'music_info_cont'})
        album_tag = summary.find('table').find('a')

        if album_tag is not None:
            musicVO.Album_Node = album_tag['href'].strip(" ")
            musicVO.Album_ID = int(musicVO.Album_Node.rsplit('/', 1)[1])

        # attrs = summary.find('li', attrs={'class': 'left_con'}).findAll('p', attrs={'class': 'right'})
        musicVO.Music_Title = tag_music_info.find('li', attrs={'class' : 'top_left'})
        if musicVO.Music_Title is not None:
            musicVO.Music_Title = musicVO.Music_Title.find('p').get_text().strip()

        try:
            left_attrs = summary.find('li', attrs={'class': 'left_con'}).findAll('p', attrs={'class' : 'left'})
            right_attrs = summary.find('li', attrs={'class': 'left_con'}).findAll('p', attrs={'class' : 'right'})

        except AttributeError:
            attrs_list = bs.find('dd', attrs={'class': 'con'})
            left_attrs = attrs_list.find('li', attrs={'class': 'left_con'}).findAll('p', attrs={'class': 'left'})
            right_attrs = attrs_list.find('li', attrs={'class': 'left_con'}).findAll('p', attrs={'class': 'right'})
            
        for i in range(0, len(left_attrs)):
            if left_attrs[i].get_text().strip() == '음악장르':
                musicVO.Genre = right_attrs[i].get_text().strip()

        line_info = bs.findAll('div', attrs={'class': 'line_info'})

        lyric = line_info[0].find('li', attrs={'id': 'lyricsText'})

        if lyric is not None:
            buffer = lyric.get_text().replace('\n', '').replace('\t', '').replace('<br/>', '\n').strip()

            # 54187 때문에 포함...특문을 아예 제거 해야하는 가???
            # 특문을 포함하되 몇몇개 사용되는 것들로??
            if '</li>' in buffer:
                buffer = buffer.split('</li>', 1)[0]
            else:
                pass

            print('버퍼 : ', buffer, len(buffer.encode('utf-8')), file=sys.stderr)
            if len(buffer.encode('utf-8')) <= Music_VO.Lyrics.type.length:
                musicVO.Lyrics = buffer

        if len(line_info) > 1:
            staffs = line_info[1].findAll('ul', attrs={'class': 'con2'})
        else:
            staffs = None

        if staffs is not None:
            for staff in staffs:
                lyricists = ''
                if staff.find('li', attrs={'class': 'title'}).get_text().strip() == '작사':
                    lyricists = staff.findAll('a')
                    if len(lyricists) != 0:
                        res = ''
                        for lyricist in lyricists:
                            res = ','.join([res, lyricist['href'].strip().rsplit('/', 1)[1]])
                        musicVO.Lyricist_ID = res.split(',', 1)[1]

                if staff.find('li', attrs={'class': 'title'}).get_text().strip() == '작곡':
                    comporsers = staff.findAll('a')
                    if len(comporsers) != 0:
                        res = ''
                        for comporser in comporsers:
                            res = ','.join([res, comporser['href'].strip().rsplit('/', 1)[1]])
                        musicVO.Composer_ID = res.split(',', 1)[1]
        try:
            db_session.merge(musicVO)
            db_session.commit()
        except InternalError:
            db_session.rollback()
            try:
                import re
                pattern = re.compile(
                    u'[^ ~`!@#$%^&*()_\-+={\[}\]:<.>/?\'\"\n\ta-zA-Z0-9\u3131-\u3163\uac00-\ud7a3]+')  # 한글 키보드 특문 영어 숫자

                musicVO.Lyrics = re.sub(pattern, ' ', musicVO.Lyrics)
                db_session.merge(musicVO)
                db_session.commit()
                cw_log({musicVO.Music_ID : 'SUCCESS[RE.Compile] - Lirics'})
            except:
                print(" 완전 rollback", file=sys.stderr)
                db_session.rollback()
                musicVO.Description = None
                db_session.merge(musicVO)
                db_session.commit()
                cw_log({musicVO.Music_ID : 'FAILURE - Lirics'})
        print('저장된 가사 : ', musicVO.Lyrics, file=sys.stderr)

def cw_log(dict_input):
    import json
    dir = '__logs__'
    if not os.path.exists(dir):
        os.mkdir(dir)
    fname = '{0}/log_track[{1}].json'.format(dir, datetime.now().date())
    with open(fname, mode='a', encoding='utf8') as f:
        json.dump(dict_input,fp=f)
        f.write('\n')

def collecting_track(start_index = 1):
    um = UrlMaker()
    cw_log({'start_id[{0}]'.format(datetime.now().date()): start_index})
    for id in range(start_index, 10000000):
        um.set_param(node=URL_Node.TRACK, end_point=id)
        # crawling_track(um)
        try:
            crawling_track(um)
        except Exception as e:
            print('exception [{0}]\n[{1}]\nID : {2}'.format(e.__class__.__name__, datetime.datetime.now(), id))
            sleep(300)
            print('sleep 해제')
            return collecting_track(id)

        sleep(0.3)

def condition_control(id):
    pass

