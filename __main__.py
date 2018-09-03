# 데이터 시작은 2009년 1월 1일부터로 한다.
# 이유 : 2007, 2008년 연간 차트 존재, but 주간 및 일간차트 존재하지 않음
# from data_manufacturer import DM_1
# from modules.collection.collect import crawling_mnet_week_chart
from VO import Music_VO
from test_module.crawlling import crawling_test


from modules.collection.urlMaker import UrlMaker
from modules.collection.collect import Collector

if __name__ == '__main__':
    # DM_1()

    # crawling_mnet_week_chart()
    # crawling_test()
    # Collector.crawling_mnet_week_chart()

    # col = Collector()
    # col.Collecting()

    print(Music_VO.query.filter_by(Singer="김건모").all())


    # a = UrlMaker()
    #
    # for year in range(2009, 2017, 1):
    #     urls = a.month_loop_url_maker(year=year)
    #     for url in urls:
    #         print(url)
