import datetime
from datetime import date
from itertools import count

class UrlMaker:

    BASE_URL = "http://www.mnet.com"
    NODE_DICT = {"TOP100_CHART": "/chart/TOP100/"}
    DATE = datetime.datetime.now()

    # def month_loop_url_maker(self, year=None, month=None, day=1):
    def url_maker_DATE_based(self):
        try:
            index_date = self.DATE.strftime("%Y%m")
            self.url = "".join([self.BASE_URL, self.NODE, index_date])
            return self.url

        except ValueError as vE:
            return None

    # def __init__(self, node = NODE_DICT["TOP100_CHART"]):
    def __init__(self, node=NODE_DICT["TOP100_CHART"]):
        self.NODE = node

    def setDate(self, DATE = None):
        self.DATE = DATE