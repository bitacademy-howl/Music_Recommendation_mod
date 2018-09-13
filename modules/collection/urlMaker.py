import datetime as dt

class URL_Node:
    TOP100_CHART = "/chart/TOP100/"
    TRACK = "track"
    ARTIST = "artist"
    ALBUM = "album"

class UrlMaker:

    BASE_URL = "http://www.mnet.com"
    NODE = ''
    END_POINT = ''

    def direct_node_connect(self, end_point):
        # 페이지를 링크로 이동하기 위해서 사용
        return "/".join([self.BASE_URL, end_point])

    def make_url(self, node='', end_point=''):
        # 외부에서 그냥 호출 가능한 함수...
        return "/".join([self.BASE_URL, str(node), str(end_point)])

    def __init__(self, node = '', end_point = ''):
        self.set_param(node=node, end_point=end_point)
        self.URL = self.make_url(node=node, end_point=end_point)
        self.setDate()

    def set_param(self, node=NODE, end_point=END_POINT):
        self.NODE = node
        self.END_POINT = end_point
        self.URL = self.make_url(self.NODE, self.END_POINT)

    def setDate(self, DATE = dt.datetime.now()):
        self.DATE = DATE

    def url_maker_DATE_based(self):
        index_date = self.DATE.strftime("%Y%m")
        self.URL = "/".join([self.BASE_URL, self.NODE, index_date])

    def __repr__(self):
        return "<{0}>\nBASE_URL : {1}\nNODE : {2}\nEND_POINT : {3}\nURL : {4}".format(type(self), self.BASE_URL, self.NODE, self.END_POINT, self.URL)