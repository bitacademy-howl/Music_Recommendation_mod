from datetime import datetime as dt
from itertools import count
from bs4 import BeautifulSoup
import pandas as pd
import collection.crawler as cw

def crawling_mnet_week_chart():
    results = []
    RESULT_DIRECTORY = '__result__'

    year = 2017

    for month in range(1, 13, 1):

        if month / 10 != 1:
            month = "0%s" % month
        page = "%s%s" % (year, month)

        url = 'http://www.mnet.com/chart/TOP100/{0}'.format(page)
        html = cw.crawling(url=url)

        now = "%s%s" % (dt.now().year, dt.now().month)
        bs = BeautifulSoup(html, 'html.parser')

        tag_tbody = bs.find('tbody')
        tags_tr = tag_tbody.findAll('tr')

        for tag_tr in tags_tr:
            tag_td = tag_tr.find('td', attrs={'class': 'MMLItemTitle'})
            title_of_song = tag_td.find('a', attrs={'class': 'MMLI_Song'})
            results.append((title_of_song.get_text()))


    title = list(set(results))


    # store
    # table = pd.DataFrame(a, columns=['title', '', '', ''])
    table = pd.DataFrame(title, columns=['title'])
    table.to_csv('{0}/mnet_weeks_100.csv'.format(RESULT_DIRECTORY))

    # for year in count(start=2009):
    #     year = 2017
    #     for month in range(1, 13, 1):
    #
    #         if month/10 != 1:
    #             month = "0%s" % month
    #         page = "%s%s"% (year, month)
    #
    #         url = 'http://www.mnet.com/chart/TOP100/{0}'.format(page)
    #         html = cw.crawling(url=url)
    #
    #         now = "%s%s" % (dt.now().year, dt.now().month)
    #         bs = BeautifulSoup(html, 'html.parser')
    #
    #         tag_tbody = bs.find('tbody')
    #         tags_tr = tag_tbody.findAll('tr')
    #
    #         for tag_tr in tags_tr:
    #             tag_td = tag_tr.find('td', attrs={'class': 'MMLItemTitle'})
    #             title_of_song = tag_td.find('a', attrs={'class': 'MMLI_Song'})
    #             print(title_of_song.get_text())




        # 끝 검출
        # if now == page:
        #     return
        # if len(tags_tr) == 0:
        #     break
        #
        # for tag_tr in tags_tr:
        #     strings = list(tag_tr.strings)
        #     name = strings[1]
        #     address = strings[3]
        #     sidogu = address.split()[:2]
        #
        #     results.append( (name, address) + tuple(sidogu) )



def crawling_mnet_month_chart():
    results = []
    RESULT_DIRECTORY = '__result__'

    # for page in count(start=200901):
    for year in count(start=2009):
        for month in range(1, 12, 1):
            page = "%s%s"% (year, month)
            url = 'http://www.mnet.com/chart/TOP100/%s' % page
            html = cw.crawling(url=url)

            bs = BeautifulSoup(html, 'html.parser')
            tag_table = bs.find('table', attrs={'class' : 'table mt20'})

            tag_tbody = tag_table.find('tbody')
            tags_tr = tag_tbody.findAll('tr')
            print(page, ":", len(tags_tr), sep=':')

            # 끝 검출
            if len(tags_tr) == 0:
                break

            for tag_tr in tags_tr:
                strings = list(tag_tr.strings)
                name = strings[1]
                address = strings[3]
                sidogu = address.split()[:2]

                results.append( (name, address) + tuple(sidogu) )

    # store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gungu'])
    table.to_csv('{0}/mnet_month_100.csv'.format(RESULT_DIRECTORY))