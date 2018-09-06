import datetime

class URL_mid_Node:
    TOP100_CHART = "/chart/TOP100/"
    TRACK = "/track/"
    ARTIST = "/artist/"

class UrlMaker:

    BASE_URL = "http://www.mnet.com"

    def url_maker_DATE_based(self):
        index_date = self.DATE.strftime("%Y%m")
        self.url = "".join([self.BASE_URL, self.NODE, index_date])
        return self.url

    def direct_node_connect(self, node):
        # 페이지를 링크로 이동하기 위해서 사용
        return "".join([self.BASE_URL, node])

    def __init__(self, node=URL_mid_Node.TOP100_CHART):
        self.NODE = node
        self.setDate()

    def setDate(self, DATE = datetime.datetime.now()):
        self.DATE = DATE